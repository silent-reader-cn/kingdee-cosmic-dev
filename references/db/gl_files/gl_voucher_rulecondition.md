# 凭证转存规则-gl_voucher_rulecondition

## 目标账簿类型-多选基础资料表 t_gl_targetaccbook

- **表名称：** 目标账簿类型-多选基础资料表
- **表名：** t_gl_targetaccbook

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_targetaccbook |  | fid |
| 2 | pk_t_gl_targetaccbook |  | fpkid |

---

## 目标账簿-多选基础资料表 t_gl_targetrulebook

- **表名称：** 目标账簿-多选基础资料表
- **表名：** t_gl_targetrulebook

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_targetrulebook_fid |  | fid |
| 2 | pk_gl_targetrulebook |  | fpkid |

---

## 凭证转存规则-主表 t_gl_vourulecon

- **表名称：** 凭证转存规则-主表
- **表名：** t_gl_vourulecon

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstrikeopre | 触发操作 | varchar | 30 |  | √ | ' ' | 触发操作,枚举: audit :审核 post :过账 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fsrcacctableid | 源科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | ftargetaccbookname | ftargetaccbookname | varchar | 500 |  | √ | ' ' |  |
| 11 | fentrymerge | 分录合并选项 | varchar | 500 |  |  | ' ' | 分录合并选项 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fexeway | 执行方式 | varchar | 30 |  | √ | ' ' | 执行方式,枚举: ontime :实时 afterwards :事后 |
| 15 | fsourceaccbookname | fsourceaccbookname | varchar | 500 |  | √ | ' ' |  |
| 16 | fismergeentry | 合并相同分录行 | bpchar | 1 |  | √ | 'A' | 合并相同分录行,枚举: A :合并 B :不合并 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | ftargetstatus | 目标凭证状态 | varchar | 30 |  | √ | ' ' | 目标凭证状态,枚举: A :暂存 B :已提交 |
| 22 | fsourceaccbooktypeid | 源账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 23 | fvoucherfilter | 凭证过滤 | varchar | 1000 |  |  | ' ' | 凭证过滤 |
| 24 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fsourcebookid | 来源账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 26 | fvoucherfilterjson | 凭证过滤JSON | varchar | 1000 |  |  | ' ' | 凭证过滤JSON |
| 27 | fentrymergedesc | 分录合并选项 | varchar | 500 |  | √ | ' ' | 分录合并选项 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 30 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 31 | fsourceaccbookid | fsourceaccbookid | int8 | 64 |  | √ | 0 |  |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_vourulecon |  | fid |
| 2 | idx_t_gl_vourulecon_createorg |  | fcreateorgid |
| 3 | idx_t_gl_vourulecon_master |  | fmasterid |
| 4 | idx_gl_vourulecon |  | fnumber |

---

## 凭证转存规则-使用范围位图表 t_gl_vourulecon_m

- **表名称：** 凭证转存规则-使用范围位图表
- **表名：** t_gl_vourulecon_m

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
| 1 | pk_t_gl_vourulecon_m |  | forgid |

---

## 凭证转存规则-多语言表 t_gl_vourulecon_l

- **表名称：** 凭证转存规则-多语言表
- **表名：** t_gl_vourulecon_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_vourulecon_l |  | fpkid |
| 2 | idx_gl_vourulecon_l |  | fid,flocaleid |

---

## 凭证转存规则-使用范围表 t_gl_vourulecon_u

- **表名称：** 凭证转存规则-使用范围表
- **表名：** t_gl_vourulecon_u

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
| 1 | pk_t_gl_vourulecon_u |  | fdataid,fuseorgid |
| 2 | idx_t_gl_vourulecon_u_uo |  | fuseorgid |
