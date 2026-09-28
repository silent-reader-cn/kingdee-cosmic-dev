# 供应商抽取方案-src_supplierpick

## 招标方式-多选基础资料表 t_src_supplierpicktype

- **表名称：** 招标方式-多选基础资料表
- **表名：** t_src_supplierpicktype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supplierpicktype |  | fid |
| 2 | idx_src_supplierpicktype_bid |  | fbasedataid |
| 3 | pk_src_supplierpicktype |  | fpkid |

---

## 数据源分录-子表 t_src_supplierpickentry

- **表名称：** 数据源分录-子表
- **表名：** t_src_supplierpickentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fschemeld | 编码 | int8 | 64 |  | √ | 0 | [供应商数据源 src_supplierscheme](../src_files/src_supplierscheme.md) |
| 6 | fpercent | 抽取比率(%) | numeric | 23 | 10 | √ | 0 | 抽取比率(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supplierpickentry_fid |  | fid |
| 2 | pk_src_supplierpickentry |  | fentryid |

---

## 采购组织-多选基础资料表 t_src_supplierpickorg

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_src_supplierpickorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supplierpickorg_bid |  | fbasedataid |
| 2 | idx_src_supplierpickorg |  | fid |
| 3 | pk_src_supplierpickorg |  | fpkid |

---

## 招标流程-多选基础资料表 t_src_supplierpickflow

- **表名称：** 招标流程-多选基础资料表
- **表名：** t_src_supplierpickflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_supplierpickflow |  | fpkid |
| 2 | idx_src_supplierpickflow |  | fid |
| 3 | idx_src_supplierpickflow_bid |  | fbasedataid |

---

## 供应商抽取方案-主表 t_src_supplierpick

- **表名称：** 供应商抽取方案-主表
- **表名：** t_src_supplierpick

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisorgcategory | 是否按采购清单的组织+品类精确匹配 | bpchar | 1 |  | √ | '1' | 是否按采购清单的组织+品类精确匹配 |
| 3 | fisautorefresh | 进入抽取界面时自动抽取 | bpchar | 1 |  | √ | '1' | 进入抽取界面时自动抽取 |
| 4 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 5 | fisbymasterid | 根据主数据内码去重 | bpchar | 1 |  | √ | '0' | 根据主数据内码去重 |
| 6 | fisopenmodel | 是否按模态方式打开抽取界面 | bpchar | 1 |  | √ | '0' | 是否按模态方式打开抽取界面 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fisallsupplier | 供应商数据源的聚合方式 | bpchar | 1 |  | √ | '1' | 供应商数据源的聚合方式,枚举: 1 :交集(各数据源的供应商交集) 2 :并集(各数据源的供应商叠加) |
| 13 | fisadd | 以追加方式抽取 | bpchar | 1 |  | √ | '1' | 以追加方式抽取 |
| 14 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 15 | fisv_id | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 16 | fname | 方案名称 | varchar | 300 |  | √ | ' ' | 方案名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcategorylevel | 品类层级 | int4 | 32 |  | √ | 0 | 品类层级 |
| 19 | fisallcategory | 供方须全部供货所选品类 | bpchar | 1 |  | √ | '1' | 供方须全部供货所选品类 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fexpertcount | 随机抽取供应商数 | int4 | 32 |  | √ | 0 | 随机抽取供应商数 |
| 22 | fisaccurate | 是否精确匹配指定品类层级 | bpchar | 1 |  | √ | '0' | 是否精确匹配指定品类层级 |
| 23 | fisbypurlist | 是否精确匹配指定的物料 | bpchar | 1 |  | √ | '0' | 是否精确匹配指定的物料 |
| 24 | fpurorglevel | 组织层级 | bpchar | 1 |  | √ | '2' | 组织层级,枚举: 1 :仅取本组织 2 :取本组织及其下级组织 3 :取本组织及同级别其他组织 4 :取本组织及同级别其他组织(含直接上级) |
| 25 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 26 | fisuninvite | 是否记录不邀请供应商 | bpchar | 1 |  | √ | '1' | 是否记录不邀请供应商,枚举: 1 :不需要记录 2 :记录不邀请供应商 3 :记录，且需要填写不邀请理由 |
| 27 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 29 | fsumvalue | 抽取比率合计 | numeric | 23 | 10 | √ | 0 | 抽取比率合计 |
| 30 | finvitetype | 抽取供应商方式 | bpchar | 1 |  | √ | '1' | 抽取供应商方式,枚举: 1 :按项目抽取供应商 2 :按标段抽取供应商 3 :按标的抽取供应商 |
| 31 | fisinviteselect | fisinviteselect | bpchar | 1 |  | √ | '1' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_supplierpick |  | fid |
| 2 | idx_src_supplierpick_num |  | fnumber |

---

## 供应商抽取方案-多语言表 t_src_supplierpick_l

- **表名称：** 供应商抽取方案-多语言表
- **表名：** t_src_supplierpick_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 300 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supplierpick_l_fid |  | fid,flocaleid |
| 2 | pk_src_supplierpick_l |  | fpkid |
