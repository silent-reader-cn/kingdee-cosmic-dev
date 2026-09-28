# 界面个性化配置-bos_newpageconfig

## 界面个性化配置-多语言表 t_cts_layoutscheme_l

- **表名称：** 界面个性化配置-多语言表
- **表名：** t_cts_layoutscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cts_layoutscheme_l |  | fpkid |
| 2 | idx_cts_layout_scheme_l_fid |  | fid,flocaleid |

---

## 字段控制-子表 t_cts_layoutfieldctl

- **表名称：** 字段控制-子表
- **表名：** t_cts_layoutfieldctl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvnew | 新增可见 | bpchar | 1 |  | √ | '0' | 新增可见 |
| 3 | fsubmitenabled | 提交锁定 | bpchar | 1 |  | √ | '0' | 提交锁定 |
| 4 | fvedit | 修改可见 | bpchar | 1 |  | √ | '0' | 修改可见 |
| 5 | fentityfieldkey | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 6 | fseq | 分录行号 | int2 | 16 |  | √ | 0 | 分录行号 |
| 7 | feditenabled | 修改锁定 | bpchar | 1 |  | √ | '0' | 修改锁定 |
| 8 | fvaudit | 审核可见 | bpchar | 1 |  | √ | '0' | 审核可见 |
| 9 | ffieldkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 10 | fauditenabled | 审核锁定 | bpchar | 1 |  | √ | '0' | 审核锁定 |
| 11 | fvview | 查看可见 | bpchar | 1 |  | √ | '0' | 查看可见 |
| 12 | fmustinput | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 13 | fdefaultvalue | 默认值 | varchar | 255 |  | √ | ' ' | 默认值 |
| 14 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 15 | fdefaultfuncparam | 字段类型 | varchar | 36 |  | √ | ' ' | 字段类型 |
| 16 | fvsubmit | 提交可见 | bpchar | 1 |  | √ | '0' | 提交可见 |
| 17 | fenabled | 新增锁定 | bpchar | 1 |  | √ | '0' | 新增锁定 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fvinit | 初始可见 | bpchar | 1 |  | √ | '0' | 初始可见 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cts_layoutfieldctl |  | fentryid |
| 2 | idx_cts_layoutfieldctl_id |  | fid |

---

## 界面个性化配置-主表 t_cts_layoutscheme

- **表名称：** 界面个性化配置-主表
- **表名：** t_cts_layoutscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fformnumber | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 D :编辑 |
| 6 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 方案编码 | varchar | 36 |  | √ | ' ' | 方案编码 |
| 12 | flayoutnumber_d | 页面布局 | varchar | 36 |  | √ | ' ' | 页面布局,枚举: |
| 13 | flayoutnumber | 页面布局 | varchar | 36 |  | √ | ' ' | 页面布局 |
| 14 | fisdefault | 默认单据类型 | bpchar | 1 |  | √ | '1' | 默认单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cts_layoutscheme |  | fid |
| 2 | idx_cts_layoutscheme_layoutid |  | flayoutnumber |
