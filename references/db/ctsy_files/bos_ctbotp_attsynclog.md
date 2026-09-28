# 附件同步记录-bos_ctbotp_attsynclog

## 附件同步记录-主表 t_ctbotp_attsynclog

- **表名称：** 附件同步记录-主表
- **表名：** t_ctbotp_attsynclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparam | 同步参数 | varchar | 100 |  | √ | ' ' | 同步参数 |
| 3 | ftsynclogid | 目标单同步记录表内码 | int8 | 64 |  | √ | 0 | 目标单同步记录表内码 |
| 4 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fatttype | 附件类型 | bpchar | 1 |  | √ | '1' | 附件类型,枚举: 1 :附件面板 2 :附件字段 |
| 6 | fattpkid | 附件表内码 | int8 | 64 |  | √ | 0 | 附件表内码 |
| 7 | ftbillid | 目标单内码 | int8 | 64 |  | √ | 0 | 目标单内码 |
| 8 | fstatus | 同步状态 | bpchar | 1 |  | √ | '0' | 同步状态,枚举: 0 :同步中 1 :同步成功 2 :同步失败 |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 10 | ffaildesc | 失败原因 | varchar | 2000 |  |  | null | 失败原因 |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | flastretrytime | 上次重试同步时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 上次重试同步时间 |
| 14 | fparam_tag | 同步参数_详情 | text | 0 |  |  | null | 同步参数_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctbotp_attsynclog_ftbillid |  | ftbillid |
| 2 | idx_ctbotp_attsynclog_flogid |  | ftsynclogid |
| 3 | pk_t_ctbotp_attsynclog |  | fid |
