# 黑白名单-fbd_pandamenu

## 名单信息分录-子表 t_fbd_pandamenuentity

- **表名称：** 名单信息分录-子表
- **表名：** t_fbd_pandamenuentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmenuname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmaterialid | 名称 | int8 | 64 |  | √ | 0 | 银行类别 bd_bankcgsetting |
| 4 | fmenuno | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fmenucusname | 自定义匹配名称（多值以分号隔开） | varchar | 100 |  | √ | ' ' | 自定义匹配名称（多值以分号隔开） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fbd_pandamenuentity |  | fentryid |
| 2 | idx_fbd_pandamenuentity |  | fid |

---

## 黑白名单-多语言表 t_fbd_pandamenu_l

- **表名称：** 黑白名单-多语言表
- **表名：** t_fbd_pandamenu_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_pandamenu_l |  | fid,flocaleid |
| 2 | pk_t_fbd_pandamenu_l |  | fpkid |

---

## 黑白名单-使用范围表 t_fbd_pandamenu_u

- **表名称：** 黑白名单-使用范围表
- **表名：** t_fbd_pandamenu_u

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
| 1 | idx_t_fbd_pandamenu_u_uo |  | fuseorgid |
| 2 | pk_t_fbd_pandamenu_u |  | fdataid,fuseorgid |

---

## 黑白名单-主表 t_fbd_pandamenu

- **表名称：** 黑白名单-主表
- **表名：** t_fbd_pandamenu

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcomment | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 80 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fbiztype | 名单类型 | varchar | 80 |  | √ | ' ' | 名单类型,枚举: bd_bankcgsetting :银行类别 bd_finorginfo :合作金融机构 bd_bebank :行名行号 bd_customer :客户 bd_supplier :供应商 bos_org :业务单元 fbd_other :其他 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fmenuprop | 名单属性 | bpchar | 1 |  | √ | ' ' | 名单属性,枚举: W :白名单 B :黑名单 |
| 20 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fbd_pandamenu_createorg |  | fcreateorgid |
| 2 | pk_fbd_pandamenu |  | fid |
| 3 | idx_t_fbd_panda_creorg |  | fcreateorgid |
| 4 | idx_t_fbd_pandamenu_master |  | fmasterid |
| 5 | idx_t_fbd_panda_master |  | fmasterid |

---

## 名单管控方案分录-子表 t_fbd_pandaschmentity

- **表名称：** 名单管控方案分录-子表
- **表名：** t_fbd_pandaschmentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillmatchidfield | 单据匹配标识字段 | varchar | 80 |  | √ | ' ' | 单据匹配标识字段 |
| 3 | fmatchway | 匹配关系 | bpchar | 1 |  | √ | ' ' | 匹配关系,枚举: E :等于 M :模糊匹配（单据字段包含名单） |
| 4 | fmenumatchfield | 名单匹配字段 | varchar | 80 |  | √ | ' ' | 名单匹配字段,枚举: menuno :编码 menuname :名称 menucusname :自定义匹配名称 |
| 5 | fbillnotifyfield | 单据匹配提示字段 | varchar | 100 |  | √ | ' ' | 单据匹配提示字段 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbillcondition | 单据适用条件 | varchar | 255 |  | √ | ' ' | 单据适用条件 |
| 8 | fbillmatchfield | 单据匹配字段 | varchar | 80 |  | √ | ' ' | 单据匹配字段 |
| 9 | fmatchtip | 匹配提示 | varchar | 80 |  | √ | ' ' | 匹配提示 |
| 10 | fbillcheckname | 单据的校验操作 | varchar | 255 |  | √ | ' ' | 单据的校验操作 |
| 11 | fschemename | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 12 | fscheme | 管控方案 | bpchar | 1 |  | √ | ' ' | 管控方案,枚举: N :不控制 Y :控制命中名单单据 R :控制未命中名单单据 W :预警命中名单单据 M :预警未命中名单单据 |
| 13 | fbizbill | 单据 | varchar | 80 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 14 | fbillcheck | 单据操作编码 | varchar | 255 |  | √ | ' ' | 单据操作编码 |
| 15 | fbillconditionval_tag | 单据适用条件值_详情 | text | 0 |  |  | ' ' | 单据适用条件值_详情 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fbillconditionval | 单据适用条件值 | varchar | 255 |  | √ | ' ' | 单据适用条件值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_pandaschmentity |  | fid |
| 2 | pk_fbd_pandaschmentity |  | fentryid |
