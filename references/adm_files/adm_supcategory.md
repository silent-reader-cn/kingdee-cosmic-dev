# 品类查询-adm_supcategory

## 品类查询-主表 t_pur_supcategory

- **表名称：** 品类查询-主表
- **表名：** t_pur_supcategory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fgroupid | 供应商分组 | int8 | 64 |  | √ | 0 | 供应商分类 bd_suppliergroup |
| 4 | fmodifierid | 最近更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fsynchrosourcelist | fsynchrosourcelist | bpchar | 1 |  | √ | '0' |  |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 8 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 srm_supplier |
| 9 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 10 | fmodifytime | 最近更新时间 | timestamp | 0 |  |  | null | 最近更新时间 |
| 11 | ffreezer | ffreezer | int8 | 64 |  | √ | 0 |  |
| 12 | fauditstatus | 当前状态 | bpchar | 1 |  | √ | '1' | 当前状态,枚举: 1 :有效 2 :无效 3 :冻结 4 :退出 |
| 13 | fissourcelist | 更新货源清单 | bpchar | 1 |  | √ | '0' | 更新货源清单 |
| 14 | fsourcelistentryid | fsourcelistentryid | varchar | 80 |  | √ | ' ' |  |
| 15 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 16 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 17 | fcategorytype | 类型 | bpchar | 1 |  | √ | 'B' | 类型,枚举: A :物料 B :品类 |
| 18 | ffreezetime | ffreezetime | timestamp | 0 |  |  | null |  |
| 19 | fexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 20 | fcategoryid | 采购品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 21 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_supcategory_pkey |  | fid |
| 2 | idx_pur_supcategory_org |  | forgid |
| 3 | idx_pur_supcategory_cat |  | fcategoryid |
| 4 | idx_pur_supcategory_sup |  | fsupplierid |
