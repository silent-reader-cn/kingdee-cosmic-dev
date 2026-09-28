# 差异项目-gl_diffitem

## 差异项目-多语言表 t_gl_diffitem_l

- **表名称：** 差异项目-多语言表
- **表名：** t_gl_diffitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 4 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_diffitem_l |  | fpkid |
| 2 | idx_gl_diffitem_l |  | fid,flocaleid |

---

## 差异项目-使用范围表 t_gl_diffitem_u

- **表名称：** 差异项目-使用范围表
- **表名：** t_gl_diffitem_u

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
| 1 | pk_t_gl_diffitem_u |  | fdataid,fuseorgid |
| 2 | idx_t_gl_diffitem_u_uo |  | fuseorgid |

---

## 差异项目-主表 t_gl_diffitem

- **表名称：** 差异项目-主表
- **表名：** t_gl_diffitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fforbidstatus | 禁用状态 | bpchar | 1 |  | √ | ' ' | 禁用状态,枚举: 0 :禁用 1 :可用 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fadjustdirection | 调节方向 | bpchar | 1 |  | √ | ' ' | 调节方向,枚举: 0 :加减 1 :加 2 :减 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 14 | fforbidderid | 禁用人 | int4 | 32 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 600 |  |  | ' ' | 名称 |
| 19 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [差异项目 gl_diffitem](../gl_files/gl_diffitem.md) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | ffullname | 长名称 | varchar | 1000 |  |  | ' ' | 长名称 |
| 22 | flongnumber | 长编码 | varchar | 200 |  | √ | ' ' | 长编码 |
| 23 | fhelpcode | 助记码 | varchar | 100 |  |  | ' ' | 助记码 |
| 24 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 26 | ftype | 项目类别 | bpchar | 1 |  | √ | '0' | 项目类别,枚举: 1 :主表项目 2 :附表项目 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 29 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gl_diffitem_master |  | fmasterid |
| 2 | idx_gl_di_num |  | fnumber |
| 3 | idx_t_gl_diffitem_createorg |  | fcreateorgid |
| 4 | idx_gl_di_org |  | forgid |
| 5 | pk_t_gl_diffitem |  | fid |
| 6 | idx_gl_di_parent |  | fparentid |
| 7 | idx_gl_di_masterid |  | fmasterid |
