# 智能审单方案-ocdbd_scheme

## 审单检查规则明细-子表 t_ocdbd_schemerule

- **表名称：** 审单检查规则明细-子表
- **表名：** t_ocdbd_schemerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetailcfgid | 详情配置 | int8 | 64 |  | √ | 0 | [详情配置 ocdbd_schema_config](../ocdbd_files/ocdbd_schema_config.md) |
| 3 | fruleenable | 启用 | bpchar | 1 |  | √ | ' ' | 启用 |
| 4 | fitem | 检查项名 | varchar | 200 |  | √ | ' ' | 检查项名 |
| 5 | fcontroltype | 单据控制方式 | varchar | 50 |  | √ | ' ' | 单据控制方式,枚举: nocontrol :不控制 confirm :提醒确认 force :严格控制 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fhandletype | 不通过处理方式 | varchar | 10 |  | √ | ' ' | 不通过处理方式,枚举: A :转人工复审 B :自动循环审单 C :不通过打回 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmanualaudit | 人工审单校验 | bpchar | 1 |  | √ | ' ' | 人工审单校验 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_schemerule |  | fid |
| 2 | pk_ocdbd_schemerule |  | fentryid |

---

## 审单优先级明细-子表 t_ocdbd_schemeent

- **表名称：** 审单优先级明细-子表
- **表名：** t_ocdbd_schemeent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 3 | fpriorityname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 4 | fsortruleid | 排序规则 | int8 | 64 |  | √ | 0 | [排序规则 ocdbd_ordersortrule](../ocdbd_files/ocdbd_ordersortrule.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsorttype | 排序方式 | varchar | 10 |  | √ | ' ' | 排序方式,枚举: 1 :顺序 2 :降序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_schemeent |  | fentryid |
| 2 | idx_ocdbd_schemeent |  | fid |

---

## 适用销售组织范围-子表 t_ocdbd_schemeorg

- **表名称：** 适用销售组织范围-子表
- **表名：** t_ocdbd_schemeorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_schemeorg |  | fentryid |
| 2 | idx_ocdbd_schemeorg |  | fid |

---

## 智能审单方案-多语言表 t_ocdbd_smartscheme_l

- **表名称：** 智能审单方案-多语言表
- **表名：** t_ocdbd_smartscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_smartscheme_l |  | fid,flocaleid |
| 2 | pk_ocdbd_smartscheme_l |  | fpkid |

---

## 通知审核人员-多选基础资料表 t_ocdbd_schemeuser

- **表名称：** 通知审核人员-多选基础资料表
- **表名：** t_ocdbd_schemeuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_schemeuser |  | fentryid,fbasedataid |
| 2 | pk_ocdbd_schemeuser |  | fpkid |

---

## 智能审单方案-主表 t_ocdbd_smartscheme

- **表名称：** 智能审单方案-主表
- **表名：** t_ocdbd_smartscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fsmartstatusfield | 智能审单状态字段 | varchar | 50 |  | √ | ' ' | 智能审单状态字段 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fordernum | 审单每批次订单量 | int4 | 32 |  | √ | 0 | 审单每批次订单量 |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | forderop | 审单操作 | varchar | 50 |  | √ | ' ' | 审单操作,枚举: |
| 10 | fispreset | 是否预设 | bpchar | 1 |  | √ | ' ' | 是否预设 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fdays | 退出循环审单（超过订单日期天数） | int4 | 32 |  | √ | 0 | 退出循环审单（超过订单日期天数） |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fbillid | 单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fschemaformula | 数据筛选条件 | text | 0 |  |  | ' ' | 数据筛选条件 |
| 20 | fsortfield | 取数排序字段 | varchar | 50 |  | √ | ' ' | 取数排序字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_smartscheme |  | fid |
| 2 | idx_ocdbd_smartscheme_num |  | fnumber |
