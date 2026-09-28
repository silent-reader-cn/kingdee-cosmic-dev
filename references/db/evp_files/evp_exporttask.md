# 电子凭证导出日志-evp_exporttask

## 电子凭证导出日志-主表 t_evp_exporttask

- **表名称：** 电子凭证导出日志-主表
- **表名：** t_evp_exporttask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 3 | finvordnum | 增值税普票数量 | int4 | 32 |  | √ | 0 | 增值税普票数量 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fefinum | 财政电子票据数量 | int4 | 32 |  | √ | 0 | 财政电子票据数量 |
| 7 | fvouchernum | 凭证数 | int4 | 32 |  | √ | 0 | 凭证数 |
| 8 | fntrenum | 非税收入缴款书数量 | int4 | 32 |  | √ | 0 | 非税收入缴款书数量 |
| 9 | feinvspclnum | 数电票专票数量 | int4 | 32 |  | √ | 0 | 数电票专票数量 |
| 10 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | '1' | 数据状态,枚举: 0 :失败 1 :成功 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fzipurl | zip地址 | varchar | 200 |  | √ | ' ' | zip地址 |
| 14 | fatrnum | 航空电子客票数量 | int4 | 32 |  | √ | 0 | 航空电子客票数量 |
| 15 | finvspclnum | 增值税专票数量 | int4 | 32 |  | √ | 0 | 增值税专票数量 |
| 16 | fbookdate | 对账单月份 | timestamp | 0 |  |  | null | 对账单月份 |
| 17 | ffailreason | 失败原因 | varchar | 500 |  | √ | ' ' | 失败原因 |
| 18 | fnumber | 任务编码 | varchar | 50 |  | √ | ' ' | 任务编码 |
| 19 | fbkrsnum | 对账单数量 | int4 | 32 |  | √ | 0 | 对账单数量 |
| 20 | feinvordnum | 数电票普票数量 | int4 | 32 |  | √ | 0 | 数电票普票数量 |
| 21 | finvtlnum | 收费公路增值税票数量 | int4 | 32 |  | √ | 0 | 收费公路增值税票数量 |
| 22 | frainum | 铁路电子客票数量 | int4 | 32 |  | √ | 0 | 铁路电子客票数量 |
| 23 | fbkernum | 回单数量 | int4 | 32 |  | √ | 0 | 回单数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evp_exporttask |  | fnumber,forgid |
| 2 | pk_t_evp_exporttask |  | fid |
