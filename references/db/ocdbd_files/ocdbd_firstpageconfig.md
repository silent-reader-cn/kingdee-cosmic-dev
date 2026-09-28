# 首页设置-ocdbd_firstpageconfig

## 首页设置-主表 t_ocdbd_firstpage

- **表名称：** 首页设置-主表
- **表名：** t_ocdbd_firstpage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 5 | fbaseviewid | 所属页面 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 12 | fportalid | fportalid | int8 | 64 |  | √ | 0 |  |
| 13 | fissyspreset | 是否系统预设 | bpchar | 1 |  | √ | '0' | 是否系统预设 |
| 14 | fschemeobjid | 首页方案 | int8 | 64 |  | √ | 0 | [首页方案 portal_scheme](../portal_files/portal_scheme.md) |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 18 | fpagetype | 页面类型 | bpchar | 1 |  | √ | ' ' | 页面类型,枚举: A :渠道门户PC端 B :渠道门户移动端 C :渠道管家PC端 D :渠道管家移动端 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_firstpage_num |  | fnumber |
| 2 | idx_t_ocdbd_firstpage_createorg |  | fcreateorgid |
| 3 | pk_ocdbd_firstpage |  | fid |
| 4 | idx_t_ocdbd_firstpage_master |  | fmasterid |

---

## 首页使用卡片设置-子表 t_ocdbd_usecardcfg

- **表名称：** 首页使用卡片设置-子表
- **表名：** t_ocdbd_usecardcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 3 | fcardtypeid | 卡片类型 | int8 | 64 |  | √ | 0 | [卡片主档 ocdbd_firstpage_cardtype](../ocdbd_files/ocdbd_firstpage_cardtype.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | flocationy | y | numeric | 23 | 10 | √ | 0 | y |
| 6 | flocationx | x | numeric | 23 | 10 | √ | 0 | x |
| 7 | flocationh | h | numeric | 23 | 10 | √ | 0 | h |
| 8 | flocationw | w | numeric | 23 | 10 | √ | 0 | w |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_usecardcfg |  | fentryid |
| 2 | idx_ocdbd_usecardcfg_fid |  | fid |

---

## 首页使用卡片设置-多语言表 t_ocdbd_usecardaccount_l

- **表名称：** 首页使用卡片设置-多语言表
- **表名：** t_ocdbd_usecardaccount_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccountname | 余额名称 | varchar | 80 |  | √ | ' ' | 余额名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_ucaccountl_eid |  | fentryid |
| 2 | pk_ocdbd_usecardaccount_l |  | fpkid |

---

## 使用产品分配-子表 t_ocdbd_showitemtype

- **表名称：** 使用产品分配-子表
- **表名：** t_ocdbd_showitemtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 顺序 | int4 | 32 |  | √ | 0 | 顺序 |
| 3 | fname | 产品分类 | varchar | 80 |  | √ | ' ' | 产品分类 |
| 4 | flinkentryid | 关联橱窗设置ID | int8 | 64 |  | √ | 0 | 关联橱窗设置ID |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_showitemtype |  | fentryid |
| 2 | idx_ocdbd_showitemtype_fid |  | fid |

---

## 首页使用卡片设置-多语言表 t_ocdbd_usecardcfg_l

- **表名称：** 首页使用卡片设置-多语言表
- **表名：** t_ocdbd_usecardcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 卡片名称 | varchar | 80 |  | √ | ' ' | 卡片名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_usecardcfgl_elid |  | fentryid,flocaleid |
| 2 | pk_ocdbd_usecardcfg_l |  | fpkid |

---

## 卡片内容详情-子表 t_ocdbd_usecardcfgdl

- **表名称：** 卡片内容详情-子表
- **表名：** t_ocdbd_usecardcfgdl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 2 | fskipform | skipform | varchar | 255 |  | √ | ' ' | skipform |
| 3 | fgroupby | groupby | varchar | 255 |  | √ | ' ' | groupby |
| 4 | ffunc | func | varchar | 255 |  | √ | ' ' | func |
| 5 | ffield | field | varchar | 255 |  | √ | ' ' | field |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fshow | show | varchar | 255 |  | √ | ' ' | show |
| 8 | ficon | icon | varchar | 255 |  | √ | ' ' | icon |
| 9 | flevel | 顺序 | int4 | 32 |  | √ | 0 | 顺序 |
| 10 | ftype | type | varchar | 255 |  | √ | ' ' | type |
| 11 | furl | pictureurl | varchar | 255 |  | √ | ' ' | pictureurl |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态 |
| 13 | ffilter | filter | varchar | 255 |  | √ | ' ' | filter |
| 14 | fplugin | plugin | varchar | 255 |  | √ | ' ' | plugin |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fformid | formid | varchar | 255 |  | √ | ' ' | formid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_usecardcfgdl |  | fdetailid |
| 2 | idx_ocdbd_usecardcfgdl_eid |  | fentryid |

---

## 关联账户-多选基础资料表 t_ocdbd_accountset

- **表名称：** 关联账户-多选基础资料表
- **表名：** t_ocdbd_accountset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_accountset |  | fentryid,fbasedataid |
| 2 | pk_ocdbd_accountset |  | fpkid |

---

## 首页使用卡片设置-子表 t_ocdbd_usecardaccount

- **表名称：** 首页使用卡片设置-子表
- **表名：** t_ocdbd_usecardaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccountname | faccountname | varchar | 80 |  | √ | ' ' |  |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 1 :启用 0 :禁用 |
| 5 | fplugin | 数据插件 | varchar | 255 |  | √ | ' ' | 数据插件 |
| 6 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_usecardaccount |  | fentryid |
| 2 | idx_ocdbd_usecardaccount_fid |  | fid |

---

## 首页设置-多语言表 t_ocdbd_firstpage_l

- **表名称：** 首页设置-多语言表
- **表名：** t_ocdbd_firstpage_l

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
| 1 | idx_ocdbd_firstpagel_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_firstpage_l |  | fpkid |

---

## 首页设置-使用范围表 t_ocdbd_firstpage_u

- **表名称：** 首页设置-使用范围表
- **表名：** t_ocdbd_firstpage_u

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
| 1 | idx_t_ocdbd_firstpage_u_uo |  | fuseorgid |
| 2 | pk_t_ocdbd_firstpage_u |  | fdataid,fuseorgid |

---

## 首页产品配置-子表 t_ocdbd_showitemdetail

- **表名称：** 首页产品配置-子表
- **表名：** t_ocdbd_showitemdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fitemid | 产品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 6 | fitemlevel | 顺序号 | int4 | 32 |  | √ | 0 | 顺序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_showitemdetail |  | fdetailid |
| 2 | idx_ocdbd_showitemdetail_eid |  | fentryid |

---

## 分配销售组织-子表 t_ocdbd_firstpage_org

- **表名称：** 分配销售组织-子表
- **表名：** t_ocdbd_firstpage_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_firstpage_org |  | fsaleorgid |
| 2 | pk_ocdbd_firstpage_org |  | fentryid |

---

## 卡片内容详情-多语言表 t_ocdbd_usecardcfgdl_l

- **表名称：** 卡片内容详情-多语言表
- **表名：** t_ocdbd_usecardcfgdl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 卡片内容名称 | varchar | 80 |  | √ | ' ' | 卡片内容名称 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_usecardcfgdl_l |  | fpkid |
| 2 | idx_ocdbd_usecardcfgdll_dlid |  | fdetailid,flocaleid |
