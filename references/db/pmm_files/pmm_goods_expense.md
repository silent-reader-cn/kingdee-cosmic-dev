# 映射费用项目-pmm_goods_expense

## 映射费用项目-使用范围表 t_mal_goodsexpense_u

- **表名称：** 映射费用项目-使用范围表
- **表名：** t_mal_goodsexpense_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_goodsexpense_u |  | fdataid,fuseorgid |
| 2 | idx_t_mal_goodsexpense_u_uo |  | fuseorgid |

---

## 映射费用项目-多语言表 t_mal_goodsexpense_l

- **表名称：** 映射费用项目-多语言表
- **表名：** t_mal_goodsexpense_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_goodsexpense_l |  | fpkid |
| 2 | idx_mal_goodsexpense_fid |  | fid,flocaleid |

---

## 映射费用项目-主表 t_mal_goodsexpense

- **表名称：** 映射费用项目-主表
- **表名：** t_mal_goodsexpense

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fgroupid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_goodsclass](../gmc_files/mdr_goodsclass.md) |
| 5 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcontroltype | 控制方式 | bpchar | 1 |  | √ | ' ' | 控制方式,枚举: 0 :单价 1 :金额 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fdisabletime | 最后禁用日期 | timestamp | 0 |  |  | null | 最后禁用日期 |
| 13 | fmodifytime | 最后更新日期 | timestamp | 0 |  |  | null | 最后更新日期 |
| 14 | fenabletime | 最后启用日期 | timestamp | 0 |  |  | null | 最后启用日期 |
| 15 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fgooduseid | 商品用途 | int8 | 64 |  | √ | 0 | [商品用途 pmm_goods_use](../pmm_files/pmm_goods_use.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 20 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_goodsexpense_crorg |  | fcreateorgid |
| 2 | idx_mal_goodsexpense_cat |  | fgroupid |
| 3 | idx_t_mal_goodsexpense_master |  | fmasterid |
| 4 | idx_mal_goodsexpense_mast |  | fmasterid |
| 5 | pk_t_mal_goodsexpense |  | fid |
| 6 | idx_t_mal_goodsexpense_createorg |  | fcreateorgid |

---

## 分录-子表 t_mal_goodsexpenseentry

- **表名称：** 分录-子表
- **表名：** t_mal_goodsexpenseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | foperator | 运算符 | varchar | 2 |  | √ | ' ' | 运算符,枚举: < :< <= :<= = := >= :>= > :> |
| 4 | fqtyto | 金额至（<） | numeric | 23 | 10 | √ | 0 | 金额至（<） |
| 5 | fcontrolview | 控制条件 | varchar | 512 |  | √ | ' ' | 控制条件 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcontrolvalue | 控制条件 | numeric | 23 | 10 | √ | 0 | 控制条件 |
| 8 | fqtyfrom | 金额从（>=） | numeric | 23 | 10 | √ | 0 | 金额从（>=） |
| 9 | fpricefrom | 单价从（>=） | numeric | 23 | 10 | √ | 0 | 单价从（>=） |
| 10 | fentryctrltype | 控制方式 | bpchar | 1 |  | √ | ' ' | 控制方式,枚举: 0 :单价 1 :金额 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fpriceto | 单价至（<） | numeric | 23 | 10 | √ | 0 | 单价至（<） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_goodsexpenseentry |  | fentryid |
| 2 | idx_mal_goodsexpenseentry_item |  | fexpenseitemid |
| 3 | idx_mal_goodsexpenseentry_fid |  | fid |
