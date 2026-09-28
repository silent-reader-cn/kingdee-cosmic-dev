# 异常日志-som_knowledge_excp

## 异常日志-主表 t_tk_scs_excption

- **表名称：** 异常日志-主表
- **表名：** t_tk_scs_excption

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fentitynum | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 4 | ferrorstack_tag | 异常堆栈_详情 | text | 0 |  |  | null | 异常堆栈_详情 |
| 5 | fbillstatus | 单据状态 | varchar | 4 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdataid | 数据id | int8 | 64 |  | √ | 0 | 数据id |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | ferrorstate | 错误类型 | varchar | 30 |  | √ | ' ' | 错误类型,枚举: |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | ferrorstack | 异常堆栈 | varchar | 255 |  | √ | ' ' | 异常堆栈 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_scs_excp_entity |  | fentitynum |
| 2 | pk_t_tk_scs_excption |  | fid |
