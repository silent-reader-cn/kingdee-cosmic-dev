# 评委考评意见F7-src_evaluateopinionf7

## 评委考评意见F7-主表 t_src_evaluateopinion

- **表名称：** 评委考评意见F7-主表
- **表名：** t_src_evaluateopinion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fscorerscore | 评委评分 | numeric | 23 | 10 | √ | 0 | 评委评分 |
| 4 | fprojectid | 考评项目 | int8 | 64 |  | √ | 0 | [专家考评F7 src_evaluatef7](../src_files/src_evaluatef7.md) |
| 5 | fgradeid | 考评等级 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 6 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fsuggestion | 考评意见 | varchar | 510 |  | √ | ' ' | 考评意见 |
| 8 | fisvalid | 是否合格 | bpchar | 1 |  | √ | '0' | 是否合格,枚举: 0 :未评审 1 :合格 2 :不合格 |
| 9 | fscoretaskid | 考评任务 | int8 | 64 |  | √ | 0 | [考评记录F7 src_evaluatetaskf7](../src_files/src_evaluatetaskf7.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evaluateopinion_sid |  | fscorerid |
| 2 | idx_src_evaluateopinion_pid |  | fprojectid |
| 3 | pk_src_evaluateopinion |  | fid |
| 4 | idx_src_evaluateopinion_tid |  | fscoretaskid |

---

## 附件-附件表 t_src_opinion_fj

- **表名称：** 附件-附件表
- **表名：** t_src_opinion_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_opinion_fj |  | fpkid |
| 2 | t_src_opinion_fj_fid |  | fid |
