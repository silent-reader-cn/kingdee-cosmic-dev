# VMI结算模型-pm_vmisettlemodel

## VMI结算模型-主表 t_pm_vmisettlemodel

- **表名称：** VMI结算模型-主表
- **表名：** t_pm_vmisettlemodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvmisettlesrcbill | VMI结算源单实体 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | ftovmisettlesrcbillrule | 物权转移单—VMI结算源单转换规则 | varchar | 36 |  | √ | ' ' | 转换规则 botp_crlist |
| 8 | ftransferbill | 物权转移单实体 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fisquoteprice | 物权转移单自动取价 | bpchar | 1 |  | √ | '1' | 物权转移单自动取价 |
| 11 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | ftotransferbillrule | VMI结算源单—物权转移单转换规则 | varchar | 36 |  | √ | ' ' | 转换规则 botp_crlist |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fispre | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 15 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fplugin | 插件 | varchar | 100 |  | √ | ' ' | 插件 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fpurinbill | 采购入库单实体 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 20 | ftopurinbillrule | 物权转移单—采购入库单转换规则 | varchar | 36 |  | √ | ' ' | 转换规则 botp_crlist |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_vmisettlemodel |  | fid |
| 2 | idx_pm_vmisettlemodel_number |  | fnumber |

---

## VMI结算模型-多语言表 t_pm_vmisettlemodel_l

- **表名称：** VMI结算模型-多语言表
- **表名：** t_pm_vmisettlemodel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pm_vmisettlemodel_l |  | fid,flocaleid |
| 2 | pk_t_pm_vmisettlemodel_l |  | fpkid |
