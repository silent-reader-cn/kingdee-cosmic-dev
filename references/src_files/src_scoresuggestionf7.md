# 评委评审意见F7-src_scoresuggestionf7

## 评委评审意见F7-主表 t_src_scoresuggestion

- **表名称：** 评委评审意见F7-主表
- **表名：** t_src_scoresuggestion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fscorerscore | 评委评分 | numeric | 23 | 10 | √ | 0 | 评委评分 |
| 4 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fsuggestion | 评审意见 | varchar | 510 |  | √ | ' ' | 评审意见 |
| 6 | fisvalid | 是否合格 | bpchar | 1 |  | √ | '0' | 是否合格,枚举: 0 :未评审 1 :合格 2 :不合格 |
| 7 | fscoretaskid | 评标任务 | int8 | 64 |  | √ | 0 | 评标任务F7 src_scoretaskf7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_scoresuggestion_sid |  | fscoretaskid |
| 2 | pk_src_scoresuggestion |  | fid |

---

## 附件-附件表 t_src_suggestion_fj

- **表名称：** 附件-附件表
- **表名：** t_src_suggestion_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_src_suggestion_fj_fid |  | fid |
| 2 | pk_src_suggestion_fj |  | fpkid |
