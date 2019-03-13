# ID3Tag Module

matchingDict = {
    'Audio encryption'                                  : 'AENC',
    'Audio seek point index'                            : 'ASPI', # 2.4
    'Attached picture'                                  : 'APIC',
    'Comments'                                          : 'COMM',
    'Commercial frame'                                  : 'COMR',
    'Encryption method registration'                    : 'ENCR',
    'Equalization'                                      : 'EQUA',
    'Equalization'                                      : 'EQU2', # 2.4
    'Event timing codes'                                : 'ETCO',
    'General encapsulated object'                       : 'GEOB',
    'Group identification registration'                 : 'GRID',
    'Grouping'                                          : 'GRP1', # Not in master list
    'Involved people list'                              : 'IPLS',
    'Involved people'                                   : 'TIPL', # 2.4
    'Linked information'                                : 'LINK',
    'Music CD identifier'                               : 'MCDI',
    'MPEG location lookup table'                        : 'MLLT',
    'Movement'                                          : 'MVIN', # Not in master list
    'Movement total'                                    : 'MVIN', # Not in master list
    'Movement name'                                     : 'MVNM', # Not in master list
    'Ownership frame'                                   : 'OWNE',
    'Private frame'                                     : 'PRIV',
    'Play counter'                                      : 'PCNT',
    'Podcast'                                           : 'PCST', # Not in master list
    'Popularimeter'                                     : 'POPM',
    'Rating MM'                                         : 'POPM', # Not in master list
    'Rating WMP'                                        : 'POPM', # Not in master list
    'Position synchronisation frame'                    : 'POSS',
    'Recommended buffer size'                           : 'RBUF',
    'Relative volume adjustment'                        : 'RVAD',
    'Relative volume adjustment'                        : 'RVA2', # 2.4
    'Reverb'                                            : 'RVRB',
    'Seek frame'                                        : 'SEEK', # 2.4
    'Signature frame'                                   : 'SIGN', # 2.4
    'Synchronized lyric/text'                           : 'SYLT',
    'Synchronized lyric'                                : 'SYLT', #
    'Synchronized text'                                 : 'SYLT', #
    'Synchronized tempo codes'                          : 'SYTC',
    'Album/Movie/Show title'                            : 'TALB',
    'Album'                                             : 'TALB', #
    'Album title'                                       : 'TALB', #
    'Movie title'                                       : 'TALB', #
    'Show title'                                        : 'TALB', #
    'Beats per minute (BPM)'                            : 'TBPM',
    'BPM'                                               : 'TBPM', #
    'Beats per minute'                                  : 'TBPM', #
    'Podcast category'                                  : 'TCAT', # Not in master list
    'Composer'                                          : 'TCOM',
    'Genre'                                             : 'TCON',
    'Content type'                                      : 'TCON', #
    'Copyright'                                         : 'TCOP',
    'Copyright message'                                 : 'TCOP', #
    'Compilation'                                       : 'TCMP', # Not in master list
    'Date'                                              : 'TDAT',
    'Date'                                              : 'TDRC', # 2.4
    'Recording time'                                    : 'TDRC', # 2.4
    'Time'                                              : 'TDRC', # 2.4
    'Encoding time'                                     : 'TDEN', # 2.4, Not in master list
    'Podcast desc'                                      : 'TDES', # Not in master list
    'Playlist delay'                                    : 'TDLY',
    'Release time'                                      : 'TDRL', # Not in master list
    'Tagging time'                                      : 'TDTG', # Not in master list
    'Encoded by'                                        : 'TENC',
    'Lyricist/Text writer'                              : 'TEXT',
    'Lyricist'                                          : 'TEXT', #
    'Text writer'                                       : 'TEXT', #
    'File type'                                         : 'TFLT',
    'Podcast ID'                                        : 'TGID', # Not in master list
    'Time'                                              : 'TIME',
    'Content group description'                         : 'TIT1',
    'Content group'                                     : 'TIT1', #
    'Title/songname/content description'                : 'TIT2',
    'Title'                                             : 'TIT2', #
    'Title description'                                 : 'TIT2', #
    'Songname description'                              : 'TIT2', #
    'Content description'                               : 'TIT2', #
    'Subtitle/Description refinement'                   : 'TIT3', 
    'Subtitle'                                          : 'TIT3', #
    'Subtitle refinement'                               : 'TIT3', #
    'Description refinement'                            : 'TIT3', #
    'Initial key'                                       : 'TKEY',
    'Podcast keywords'                                  : 'TKWD', # Not in master list
    'Language'                                          : 'TLAN',
    'Length'                                            : 'TLEN',
    'Musician credits'                                  : 'TMCL', # Not in master list
    'Musician credits list'                             : 'TMCL', # Not in master list
    'Media type'                                        : 'TMED',
    'Mood'                                              : 'TMOO', # Not in master list
    'Original album/move/show title'                    : 'TOAL',
    'Orig album'                                        : 'TOAL', #
    'Original album'                                    : 'TOAL', #
    'Original album title'                              : 'TOAL', #
    'Orig movie'                                        : 'TOAL', #
    'Original movie'                                    : 'TOAL', #
    'Original movie title'                              : 'TOAL', #
    'Orig show'                                         : 'TOAL', #
    'Original show'                                     : 'TOAL', #
    'Original show title'                               : 'TOAL', #
    'Orig filename'                                     : 'TOFN',
    'Original filename'                                 : 'TOFN', #
    'Original lyricist/text writer'                     : 'TOLY',
    'Orig lyricist'                                     : 'TOLY', #
    'Original lyricist'                                 : 'TOLY', #
    'Original lyricist writer'                          : 'TOLY', #
    'Orig text'                                         : 'TOLY', #
    'Original text'                                     : 'TOLY', #
    'Original text writer'                              : 'TOLY', #
    'Original artist/performer'                         : 'TOPE',
    'Orig artist'                                       : 'TOPE', #
    'Original artist'                                   : 'TOPE', #
    'Original performer'                                : 'TOPE', #
    'Orig year'                                         : 'TORY',
    'Original release year'                             : 'TORY', #
    'Orig year'                                         : 'TDOR', # 2.4 
    'Original release year'                             : 'TDOR', # 2.4 
    'File owner/licensee'                               : 'TOWN',
    'File owner'                                        : 'TOWN', #
    'Licensee'                                          : 'TOWN', #
    'Artist'                                            : 'TPE1',
    'Lead performer/Soloist'                            : 'TPE1', #
    'Lead performer'                                    : 'TPE1', #
    'Soloist'                                           : 'TPE1', #
    'Album artist'                                      : 'TPE2',
    'Band/orchestra/accompaniment'                      : 'TPE2', #
    'Band'                                              : 'TPE2', #
    'Orchestra'                                         : 'TPE2', #
    'Accompaniment'                                     : 'TPE2', #
    'Conductor'                                         : 'TPE3',
    'Conductor/performer refinement'                    : 'TPE3', #
    'Conductor refinement'                              : 'TPE3', #
    'Performer refinement'                              : 'TPE3', #
    'Mix artist'                                        : 'TPE4',
    'Interpreted, remixed, or otherwise modified by'    : 'TPE4', #
    'Disc number'                                       : 'TPOS',
    'Part of a set'                                     : 'TPOS', #
    'Produced notice'                                   : 'TPRO', # 2.4
    'Publisher'                                         : 'TPUB',
    'Organization'                                      : 'TPUB', # Custom
    'Track'                                             : 'TRCK',
    'Track number/Position in set'                      : 'TRCK', #
    'Track number'                                      : 'TRCK', #
    'Position in set'                                   : 'TRCK', #
    'Recording dates'                                   : 'TRDA',
    'Recording dates'                                   : 'TDRC', # 2.4
    'Net radio station'                                 : 'TRSN',
    'Internet radio station name'                       : 'TRSN', #
    'Net radio owner'                                   : 'TRSO',
    'Internet radio station owner'                      : 'TRSO', #
    'Album artist sort'                                 : 'TSO2', # Not in master list
    'Album sort'                                        : 'TSOA', # 2.4, Not in master list
    'Composer sort'                                     : 'TSOC', # Not in master list
    'Artist sort'                                       : 'TSOP', # 2.4, Not in master list
    'Title sort'                                        : 'TSOT', # 2.4, Not in master list
    'Size'                                              : 'TSIZ',
    'International Standard Recording Code (ISRC)'      : 'TSRC',
    'ISRC'                                              : 'TSRC', #
    'International standard recording code'             : 'TSRC', #
    'Encoder settings'                                  : 'TSSE',
    'Software/Hardware and settings used for encoding'  : 'TSSE', #
    'Software and settings used for encoding'           : 'TSSE', #
    'Hardware and settings used for encoding'           : 'TSSE', #
    'Set subtitle'                                      : 'TSST', # 2.4
    'Year'                                              : 'TYER',
    'Year'                                              : 'TDRC', # 2.4
    #'User defined text information frame'               : 'TXXX',
    'Unique file identifier'                            : 'UFID',
    'Terms of use'                                      : 'USER',
    'Unsynced lyrics'                                   : 'USLT',
    'Unsynchronized lyric/text transcription'           : 'USLT', #
    'Unsynchronized lyric'                              : 'USLT', #
    'Unsynchronized lyric transcription'                : 'USLT', #
    'Unsynced text'                                     : 'USLT', #
    'Unsynchronized text'                               : 'USLT', #
    'Unsynchronized text transcription'                 : 'USLT', #
    'WWW Commercial info'                               : 'WCOM',
    'Commercial information'                            : 'WCOM', #
    'WWW Copyright'                                     : 'WCOP',
    'Copyright information'                             : 'WCOP', #
    'Legal information'                                 : 'WCOP', #
    'Podcast URL'                                       : 'WFED', # Not in master list
    'WWW audio file'                                    : 'WOAF',
    'Official audio file webpage'                       : 'WOAF', #
    'WWW artist'                                        : 'WOAR',
    'Official artist webpage'                           : 'WOAR', #
    'Official performer webpage'                        : 'WOAR', #
    'WWW audio source'                                  : 'WOAS',
    'Official audio source webpage'                     : 'WOAS', #
    'WWW radio page'                                    : 'WORS',
    'Official internet radio station homepage'          : 'WORS', #
    'WWW Payment'                                       : 'WPAY',
    'Payment'                                           : 'WPAY', #
    'WWW Publisher'                                     : 'WPUB',
    'Publishers official webpage'                       : 'WPUB', #
    #'User defined URL link frame'                       : 'WXXX'
    }

matchingStrings = matchingDict.keys()
