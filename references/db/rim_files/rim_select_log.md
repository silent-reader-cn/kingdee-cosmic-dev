# 勾选认证日志-rim_select_log

## 勾选认证日志-主表 t_rim_select_log

- **表名称：** 勾选认证日志-主表
- **表名：** t_rim_select_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forg_id | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | finvoice_amount | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 4 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 5 | fupdate_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 6 | fresult_json | json数据 | varchar | 255 |  | √ | ' ' | json数据 |
| 7 | fbatch_no | 批次号 | varchar | 36 |  | √ | ' ' | 批次号 |
| 8 | ftotal_tax_amount | 发票税额 | numeric | 23 | 10 | √ | 0 | 发票税额 |
| 9 | ftax_no | 税号 | varchar | 20 |  | √ | ' ' | 税号 |
| 10 | fselect_type | 勾选认证类型 | varchar | 2 |  | √ | ' ' | 勾选认证类型,枚举: 1 :同步勾选 2 :异步勾选 4 :旅客运输抵扣 5 :预勾选 6 :认证 |
| 11 | fresult_json_tag | json数据_详情 | text | 0 |  |  | null | json数据_详情 |
| 12 | fdescription | 描述信息 | varchar | 120 |  | √ | ' ' | 描述信息 |
| 13 | ftax_period | 抵扣税期 | timestamp | 0 |  |  | null | 抵扣税期 |
| 14 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 10 | √ | 0 | 可抵扣税额 |
| 15 | ffail_num | 失败份数 | int4 | 32 |  | √ | 0 | 失败份数 |
| 16 | fsuccess_num | 成功份数 | int4 | 32 |  | √ | 0 | 成功份数 |
| 17 | fselect_opera_type | 操作方式 | varchar | 2 |  | √ | ' ' | 操作方式,枚举: 1 :手工操作 2 :自动操作 |
| 18 | fhandle_status | 处理状态 | varchar | 2 |  | √ | ' ' | 处理状态,枚举: 0 :未处理 3 :处理中 1 :成功 2 :失败 |
| 19 | fcreater | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | foperate_type | 操作类型 | varchar | 2 |  | √ | ' ' | 操作类型,枚举: 1 :抵扣勾选 -1 :撤销抵扣勾选 4 :不抵扣勾选 -4 :撤销不抵扣勾选 5 :预勾选 -5 :撤销预勾选 6 :旅客运输抵扣 -6 :撤销旅客运输抵扣 7 :生成统计表 -7 :撤销统计表 8 :确认签名 9 :批量认证 |
| 22 | fstatistics_status | 统计表状态 | varchar | 2 |  | √ | ' ' | 统计表状态,枚举: 01 :未生成统计报表 02 :已生成统计报表，并可以进行确认签名 03 :预统计(未到申报期) 04 :已生成统计报表，但不能进行确认签名 05 :已确认签名 21 :统计报表生成中 22 :没有符合条件的记录, 请先勾选发票，然后生成统计报表 23 :转登记纳税人不能进行当前统计 24 :统计报表认证中 25 :预统计，撤销统计表后再生成，才能进行确认签名 |
| 23 | ftotal_num | 发票总份数 | int4 | 32 |  | √ | 0 | 发票总份数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_select_log_createtime |  | fcreate_time |
| 2 | idx_rim_select_log_user |  | fcreater |
| 3 | idx_rim_select_log_batchno |  | fbatch_no |
| 4 | idx_rim_select_log_taxno |  | ftax_no |
| 5 | pk_t_rim_select_log |  | fid |
| 6 | idx_rim_select_log_org |  | forg_id |
