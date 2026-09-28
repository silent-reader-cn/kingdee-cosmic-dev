# 商品授权-pmm_prodadmin

## 商品授权-使用范围表 t_mal_prodadmin_u

- **表名称：** 商品授权-使用范围表
- **表名：** t_mal_prodadmin_u

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
| 1 | pk_t_mal_prodadmin_u |  | fdataid,fuseorgid |
| 2 | idx_t_mal_prodadmin_u_uo |  | fuseorgid |

---

## 商品授权-多语言表 t_mal_prodadmin_l

- **表名称：** 商品授权-多语言表
- **表名：** t_mal_prodadmin_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_prodadmin_l_pkey |  | fpkid |
| 2 | idx_mal_prodadmin_l_fid |  | fid,flocaleid |

---

## 商品授权-使用范围位图表 t_mal_prodadmin_m

- **表名称：** 商品授权-使用范围位图表
- **表名：** t_mal_prodadmin_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_prodadmin_m |  | forgid |

---

## 商品分录-子表 t_mal_prodadminentry

- **表名称：** 商品分录-子表
- **表名：** t_mal_prodadminentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 pbd_goodsclass](../pbd_files/pbd_goodsclass.md) |
| 3 | fgoodsid | 商品 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_prodadmin_fgoodsid |  | fclassid,fgoodsid |
| 2 | t_mal_prodadminentry_pkey |  | fentryid |
| 3 | idx_mal_prodadmin_fid_fseq |  | fid,fseq |

---

## 商品授权-主表 t_mal_prodadmin

- **表名称：** 商品授权-主表
- **表名：** t_mal_prodadmin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsource | 商品来源 | bpchar | 1 |  | √ | ' ' | 商品来源,枚举: 1 :内部商城 2 :京东商城 |
| 6 | fcontrolstatus | fcontrolstatus | bpchar | 1 |  | √ | ' ' |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 17 | forgscope | 方案适用范围 | bpchar | 1 |  | √ | ' ' | 方案适用范围,枚举: 1 :所有业务组织 2 :指定业务组织 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 24 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mal_prodadmin_master |  | fmasterid |
| 2 | idx_mal_prodadmin_fnumber |  | fnumber |
| 3 | idx_t_mal_prodadmin_createorg |  | fcreateorgid |
| 4 | t_mal_prodadmin_pkey |  | fid |

---

## 适用的业务组织(可多选)-多选基础资料表 t_pur_goodsadmin_org

- **表名称：** 适用的业务组织(可多选)-多选基础资料表
- **表名：** t_pur_goodsadmin_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
