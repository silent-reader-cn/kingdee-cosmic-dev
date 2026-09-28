# 营销费用类型-ocdbd_expensetype

## 营销费用类型-主表 t_ocdbd_expensetype

- **表名称：** 营销费用类型-主表
- **表名：** t_ocdbd_expensetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 5 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 6 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffullname | ffullname | varchar | 1000 |  | √ | ' ' |  |
| 9 | flongnumber | 长编码 | varchar | 1000 |  | √ | ' ' | 长编码 |
| 10 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 11 | fexpensetype | 费用类型 | bpchar | 1 |  | √ | ' ' | 费用类型,枚举: A :固定预算 B :变动预算 C :固定+变动 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcontrol | 控制粒度 | varchar | 80 |  | √ | ' ' | 控制粒度,枚举: 1 :行政组织（部门） 2 :渠道 3 :产品 4 :产品分类 5 :渠道分类 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fmustinputtype | 费用录入方式 | bpchar | 1 |  | √ | 'C' | 费用录入方式,枚举: A :录入产品数量单价 B :录入产品和申请金额 C :录入产品和数量或金额 |
| 21 | fifbudget | 是否启用预算 | bpchar | 1 |  | √ | '0' | 是否启用预算 |
| 22 | faccountid | 默认费用资金池 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 23 | ftypesign | 费用行类型 | bpchar | 1 |  | √ | 'C' | 费用行类型,枚举: A :现金类 B :物料类 C :两者都有 |
| 24 | ffeecashtypeid | 默认兑付方式 | int8 | 64 |  | √ | 0 | [费用兑付方式 ocdbd_feecashtype](../ocmem_files/ocdbd_feecashtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_expensetype_no |  | fnumber |
| 2 | pk_ocdbd_expensetype |  | fid |

---

## 营销费用类型-多语言表 t_ocdbd_expensetype_l

- **表名称：** 营销费用类型-多语言表
- **表名：** t_ocdbd_expensetype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 1000 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_expensetypel_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_expensetype_l |  | fpkid |
