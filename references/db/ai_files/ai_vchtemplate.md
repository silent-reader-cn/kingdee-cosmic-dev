# 凭证模板-ai_vchtemplate

## 凭证模板-使用范围表 t_ai_vchtemplate_u

- **表名称：** 凭证模板-使用范围表
- **表名：** t_ai_vchtemplate_u

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
| 1 | idx_t_ai_vchtemplate_u_uo |  | fuseorgid |
| 2 | t_ai_vchtemplate_u_pkey |  | fdataid,fuseorgid |

---

## 凭证模板-主表 t_ai_vchtemplate

- **表名称：** 凭证模板-主表
- **表名：** t_ai_vchtemplate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxml | 模板配置内容 | text | 0 |  |  | null | 模板配置内容 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | faccttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fxmllang | fxmllang | text | 0 |  |  | ' ' |  |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fissyspreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 14 | fvchtypedesc | 凭证类型 | varchar | 500 |  | √ | ' ' | 凭证类型 |
| 15 | fbillno | fbillno | varchar | 80 |  | √ | ' ' |  |
| 16 | feventclassid | 事件 | int8 | 64 |  | √ | 0 | [异构数据对接模型 ai_eventclass](../ai_files/ai_eventclass.md) |
| 17 | fbizdatedesc | 业务日期 | varchar | 500 |  | √ | ' ' | 业务日期 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | freoper | 关联操作 | varchar | 30 |  | √ | ' ' | 关联操作,枚举: |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 22 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | 'C' |  |
| 23 | fnewsortorder | 新凭证分录顺序 | varchar | 255 |  | √ | ' ' | 新凭证分录顺序 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | foper | 触发操作 | varchar | 30 |  | √ | ' ' | 触发操作,枚举: |
| 26 | funoper | 反操作节点 | varchar | 30 |  | √ | ' ' | 反操作节点,枚举: |
| 27 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 28 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 29 | fsourcebill | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 30 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 31 | fpresetnumber | 预置模板编码 | varchar | 80 |  | √ | ' ' | 预置模板编码 |
| 32 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 33 | facctorgid | 业务单元 | varchar | 100 |  | √ | ' ' | 业务单元 |
| 34 | fenable | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fbuildvchgen | 生成方式 | varchar | 30 |  | √ | ' ' | 生成方式,枚举: |
| 36 | fvoucherdatedesc | 记账日期 | varchar | 500 |  | √ | ' ' | 记账日期 |
| 37 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 38 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 39 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_vchtemplate_pkey |  | fid |
| 2 | idx_ai_vchtemplate_sbill |  | fsourcebill |
| 3 | idx_t_ai_vchtemplate_createorg |  | fcreateorgid |
| 4 | idx_t_ai_vchtemplate_master |  | fmasterid |

---

## 凭证模板-使用范围位图表 t_ai_vchtemplate_m

- **表名称：** 凭证模板-使用范围位图表
- **表名：** t_ai_vchtemplate_m

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
| 1 | pk_t_ai_vchtemplate_m |  | forgid |

---

## 凭证模板-多语言表 t_ai_vchtemplate_l

- **表名称：** 凭证模板-多语言表
- **表名：** t_ai_vchtemplate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fxmllang | 模板多语言内容 | text | 0 |  |  | null | 模板多语言内容 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 6 | facctbookname | facctbookname | varchar | 500 |  |  | ' ' |  |
| 7 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_vchtemplate_l_pkey |  | fpkid |
| 2 | idx_ai_vchtemplate_l_fid |  | fid,flocaleid |

---

## 适用账簿-多选基础资料表 t_ai_vchtemplate_book

- **表名称：** 适用账簿-多选基础资料表
- **表名：** t_ai_vchtemplate_book

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_vchtemp_book_ab |  | fbasedataid |
| 2 | idx_ai_vchtemp_book_fid |  | fid |
| 3 | pk_ai_vchtemplate_book |  | fpkid |

---

## 账簿类型-多选基础资料表 t_ai_vchbooktypes

- **表名称：** 账簿类型-多选基础资料表
- **表名：** t_ai_vchbooktypes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_vchbooktypes |  | fpkid |
| 2 | idx_ai_vchbooktypes |  | fid |
