# VMI结算日志-pm_vmisettlelog

## 单据体-子表 t_pm_vmisettlelogentry

- **表名称：** 单据体-子表
- **表名：** t_pm_vmisettlelogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvirtualbillentity | 虚单单据实体 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | fvirtualbillno | 虚单单据编号 | varchar | 80 |  | √ | ' ' | 虚单单据编号 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fvirtualbillid | 虚单单据id | int8 | 64 |  | √ | 0 | 虚单单据id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_vmisettlelogentry_id |  | fid |
| 2 | pk_t_pm_vmisettlelogentry |  | fentryid |

---

## VMI结算日志-主表 t_pm_vmisettlelog

- **表名称：** VMI结算日志-主表
- **表名：** t_pm_vmisettlelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpurinbillnumber | 采购入库虚单编号 | varchar | 80 |  | √ | ' ' | 采购入库虚单编号 |
| 3 | fvmisettlesrcbillid | VMI结算源单ID | int8 | 64 |  | √ | 0 | VMI结算源单ID |
| 4 | fsettletype | 结算方式 | varchar | 5 |  | √ | ' ' | 结算方式,枚举: A :手工结算 B :实时结算 C :周期结算 |
| 5 | fissuccess | 结算结果 | bpchar | 1 |  | √ | '1' | 结算结果,枚举: A :成功 B :失败 |
| 6 | ftransferbillentity | 物权转移单实体 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 7 | fsettleresult | 失败原因 | varchar | 512 |  |  | null | 失败原因 |
| 8 | fsettlelotno | 结算批号 | varchar | 80 |  | √ | ' ' | 结算批号 |
| 9 | fsettleresult_tag | 失败原因_详情 | text | 0 |  |  | null | 失败原因_详情 |
| 10 | fdatetime | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 11 | fvmisettlesrcbillnumber | VMI结算源单编号 | varchar | 80 |  | √ | ' ' | VMI结算源单编号 |
| 12 | fvmisettlesrcbillentity | VMI结算源单实体 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 13 | fvmisettlebillnumber | VMI结算虚单编号 | varchar | 80 |  | √ | ' ' | VMI结算虚单编号 |
| 14 | fpurinbillid | 采购入库虚单ID | int8 | 64 |  | √ | 0 | 采购入库虚单ID |
| 15 | fvmisettlebillid | VMI结算虚单ID | int8 | 64 |  | √ | 0 | VMI结算虚单ID |
| 16 | fsettleuserid | 结算人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fpurinbillentity | 采购入库虚单实体 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 18 | ftransferbillnumber | 物权转移单编号 | varchar | 80 |  | √ | ' ' | 物权转移单编号 |
| 19 | fvmisettlebillentity | VMI结算虚单实体 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 20 | fsettledate | 结算日期 | timestamp | 0 |  |  | null | 结算日期 |
| 21 | ftransferbillid | 物权转移单ID | int8 | 64 |  | √ | 0 | 物权转移单ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_vmisettlelog |  | fid |
| 2 | idx_pm_vmisettlelog_settleinfo |  | fsettleuserid,fsettledate,fissuccess |
