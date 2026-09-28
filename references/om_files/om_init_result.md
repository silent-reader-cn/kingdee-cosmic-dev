# 结束委外初始化-om_init_result

## 结束委外初始化-主表 t_om_initresult

- **表名称：** 结束委外初始化-主表
- **表名：** t_om_initresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fendinitdate | 结束初始化日期 | timestamp | 0 |  |  | null | 结束初始化日期 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fstartinitdate | 启用初始化日期 | timestamp | 0 |  |  | null | 启用初始化日期 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fendinitstatus | 结束初始化状态 | varchar | 50 |  | √ | ' ' | 结束初始化状态,枚举: A :未初始化 B :已初始化 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fstartinitstatus | 启用初始化状态 | varchar | 50 |  | √ | ' ' | 启用初始化状态,枚举: A :未启用 B :已启用 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_initresult |  | fid |
| 2 | idx_om_initresult_org |  | forgid |
