# 商品销售属性-ocdbd_item_saleattr

## 商品销售属性-主表 t_ocdbd_item_saleattr

- **表名称：** 商品销售属性-主表
- **表名：** t_ocdbd_item_saleattr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmulcombofies | 分销范围 | varchar | 50 |  | √ | 'A ' | 分销范围,枚举: 1 :分销 2 :零售 |
| 3 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fname | 销售属性名称 | varchar | 100 |  | √ | ' ' | 销售属性名称 |
| 5 | fisrebate | 参与返利 | bpchar | 1 |  | √ | '0' | 参与返利 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fctrlstrategy | 共享策略 | varchar | 10 |  | √ | ' ' | 共享策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 销售属性编码 | varchar | 80 |  | √ | ' ' | 销售属性编码 |
| 19 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 20 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_itemsaleattr_num |  | fnumber |
| 2 | pk_ocdbd_item_saleattr |  | fid |
| 3 | idx_t_ocdbd_item_saleattr_createorg |  | fcreateorgid |
| 4 | idx_t_ocdbd_item_saleattr_master |  | fmasterid |

---

## 商品销售属性-使用范围表 t_ocdbd_item_saleattr_u

- **表名称：** 商品销售属性-使用范围表
- **表名：** t_ocdbd_item_saleattr_u

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
| 1 | pk_t_ocdbd_item_saleattr_u |  | fdataid,fuseorgid |
| 2 | idx_t_ocdbd_item_saleattr_u_uo |  | fuseorgid |

---

## 商品销售属性-多语言表 t_ocdbd_item_saleattr_l

- **表名称：** 商品销售属性-多语言表
- **表名：** t_ocdbd_item_saleattr_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 销售属性名称 | varchar | 100 |  | √ | ' ' | 销售属性名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_item_saleattr_l |  | fpkid |
| 2 | idx_ocdbd_itemsaleal_flid |  | fid,flocaleid |
