// Vote storage and management
class VoteManager {
    constructor() {
        this.loadVotes();
    }

    // Load all votes from sessionStorage
    loadVotes() {
        try {
            const votesData = sessionStorage.getItem('all_votes');
            this.votes = votesData ? JSON.parse(votesData) : {};
            this.voteCountsByBatch = {};
            
            // Calculate current counts per batch
            Object.values(this.votes).forEach(vote => {
                this.voteCountsByBatch[vote.batch] = (this.voteCountsByBatch[vote.batch] || 0) + 1;
            });
        } catch (err) {
            console.error('Error loading votes:', err);
            this.votes = {};
            this.voteCountsByBatch = {};
        }
    }

    // Save all votes to sessionStorage
    saveVotes() {
        try {
            sessionStorage.setItem('all_votes', JSON.stringify(this.votes));
        } catch (err) {
            console.error('Error saving votes:', err);
            throw err;
        }
    }

    // Record a new vote
    recordVote(batch, position1, position2) {
        // Backwards-compatible: store two-position vote under same structure
        return this.recordFullVote(batch, { position1, position2 });
    }

    // Record a full vote with multiple positions (selections is an object mapping post->choice)
    recordFullVote(batch, selections) {
        const voteCount = this.voteCountsByBatch[batch] || 0;

        const voteId = `${batch}_voter_${voteCount + 1}`;

        const vote = {
            id: voteId,
            batch: batch,
            voterNumber: voteCount + 1,
            selections: selections,
            timestamp: new Date().toISOString()
        };

        this.votes[voteId] = vote;
        this.voteCountsByBatch[batch] = voteCount + 1;
        this.saveVotes();

        return vote;
    }

    // Get all votes for a batch
    getVotesForBatch(batch) {
        return Object.values(this.votes).filter(v => v.batch === batch);
    }

    // Get vote count for a batch
    getVoteCount(batch) {
        return this.voteCountsByBatch[batch] || 0;
    }

    // Get total votes across all batches
    getTotalVotes() {
        return Object.keys(this.votes).length;
    }

    // Check if maximum votes reached for batch (limit 30 per batch)
    isBatchFull(batch) {
        return this.getVoteCount(batch) >= 30;
    }
}

// Create global instance
window.voteManager = new VoteManager();