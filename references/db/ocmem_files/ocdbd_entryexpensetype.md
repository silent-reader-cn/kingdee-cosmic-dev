# 费用行类型-ocdbd_entryexpensetype

## 费用行类型-多语言表 t_ocdbd_eexpense_type_l

- **表名称：** 费用行类型-多语言表
- **表名：** t_ocdbd_eexpense_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_eexpensetype_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_eexpense_type_l |  | fpkid |

---

## 费用行类型-主表 t_ocdbd_eexpense_type

- **表名称：** 费用行类型-主表
- **表名：** t_ocdbd_eexpense_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ftypesign | 类型标识 | bpchar | 1 |  | √ | ' ' | 类型标识,枚举: A :现金类 B :物料类 C :其他 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_eexpense_type |  | fid |
| 2 | idx_ocdbd_eexpensetype_no |  | fnumber |

---

## 行核销方式分录-子表 t_ocdbd_subexpensetype

- **表名称：** 行核销方式分录-子表
- **表名：** t_ocdbd_subexpensetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwriteoff | fwriteoff | bpchar | 1 |  | √ | 'A' |  |
| 3 | fwriteoffno | 核销方式编码 | varchar | 80 |  | √ | ' ' | 核销方式编码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fwriteoffname | 核销方式名称 | varchar | 80 |  | √ | ' ' | 核销方式名称 |
| 6 | fentryname | 行类型名称 | varchar | 80 |  | √ | ' ' | 行类型名称 |
| 7 | fmustinputtype | 产品必录信息 | bpchar | 1 |  | √ | ' ' | 产品必录信息,枚举: A :录入产品数量单价 B :录入产品和申请金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fwriteoffaccountid | 核销结转到关联账户 | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 10 | ffeecashtypeid | 费用兑付方式 | int8 | 64 |  | √ | 0 | 费用兑付方式 ocdbd_feecashtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_subexpensetype |  | fentryid |
| 2 | idx_ocdbd_subexpensetype_fid |  | fid |
