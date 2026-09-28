# 流程内事件-wf_processevent

## 单据体-子表 t_wf_processevententry

- **表名称：** 单据体-子表
- **表名：** t_wf_processevententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrynumber | 参数编码 | varchar | 50 |  | √ | ' ' | 参数编码 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentrydesc | 参数描述 | varchar | 500 |  | √ | ' ' | 参数描述 |
| 5 | fentryname | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_procevententry_fid |  | fid |
| 2 | pk_wf_processevententry |  | fentryid |

---

## 流程内事件-主表 t_wf_processevent

- **表名称：** 流程内事件-主表
- **表名：** t_wf_processevent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | feventname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | feventnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 4 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 5 | fnumber | 唯一性编码 | int4 | 32 |  | √ | 0 | 唯一性编码 |
| 6 | feventdesc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_processevent |  | fid |
| 2 | idx_wf_procevtuniquenumber |  | fnumber |
| 3 | idx_wf_procevt_evtnumbername |  | feventnumber,feventname |

---

## 流程内事件-多语言表 t_wf_processevent_l

- **表名称：** 流程内事件-多语言表
- **表名：** t_wf_processevent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feventname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | feventdesc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_processevent_l |  | fpkid |
| 2 | idx_wf_processevent_l |  | fid,flocaleid |

---

## 单据体-多语言表 t_wf_processevententry_l

- **表名称：** 单据体-多语言表
- **表名：** t_wf_processevententry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentrydesc | 参数描述 | varchar | 500 |  | √ | ' ' | 参数描述 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fentryname | 参数名称 | varchar | 500 |  | √ | ' ' | 参数名称 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_processevententry_l |  | fentryid,flocaleid |
| 2 | pk_wf_processevententry_l |  | fpkid |
