# 标准事件分类-ai_standardevent

## 标准事件分类-多语言表 t_ai_standardevent_l

- **表名称：** 标准事件分类-多语言表
- **表名：** t_ai_standardevent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_standardevent_l |  | fpkid |
| 2 | idx_ai_standardevent_l_fid |  | fid |

---

## 单据体-子表 t_ai_standardevententity

- **表名称：** 单据体-子表
- **表名：** t_ai_standardevententity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpdesc | 取字段表达式 | varchar | 255 |  | √ | ' ' | 取字段表达式 |
| 3 | ffield | 单据字段 | varchar | 255 |  | √ | ' ' | 单据字段 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 1 | 分录行号 |
| 5 | fbilltypename | 单据类型 | varchar | 255 |  | √ | ' ' | 单据类型 |
| 6 | ffullfield | 取单据字段值 | varchar | 255 |  | √ | ' ' | 取单据字段值,枚举: |
| 7 | fasstacttypeid | 业务维度 | int8 | 64 |  | √ | 0 | [业务维度 ai_asstacttype](../ai_files/ai_asstacttype.md) |
| 8 | fexp | 取字段表达式计算公式 | varchar | 255 |  | √ | ' ' | 取字段表达式计算公式 |
| 9 | fbillid | 单据id | varchar | 50 |  | √ | ' ' | 单据id |
| 10 | frowfield | 本行可取单据字段 | varchar | 50 |  | √ | ' ' | 本行可取单据字段 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fbillno | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 13 | fbillorevent | 单据/会计事件 | bpchar | 1 |  | √ | '1' | 单据/会计事件,枚举: 1 :单据 2 :会计事件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ai_standardevententity |  | fid |
| 2 | pk_t_ai_standardevententity |  | fentryid |

---

## 单据类型-多选基础资料表 t_ai_morebilltype

- **表名称：** 单据类型-多选基础资料表
- **表名：** t_ai_morebilltype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_morebilltype |  | fpkid |
| 2 | index_ai_morebilltype |  | fid |

---

## 业务维度-多选基础资料表 t_ai_moreasstacttype

- **表名称：** 业务维度-多选基础资料表
- **表名：** t_ai_moreasstacttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务维度 ai_asstacttype](../ai_files/ai_asstacttype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ai_moreasstacttype |  | fid |
| 2 | pk_t_ai_moreasstacttype |  | fpkid |

---

## 标准事件分类-主表 t_ai_standardevent

- **表名称：** 标准事件分类-主表
- **表名：** t_ai_standardevent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_standardevent |  | fid |
| 2 | idx_ai_standardevent |  | fnumber |

---

## 事件类型-多选基础资料表 t_ai_moreeventtype

- **表名称：** 事件类型-多选基础资料表
- **表名：** t_ai_moreeventtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [异构数据对接模型 ai_eventclass](../ai_files/ai_eventclass.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_moreeventtype |  | fpkid |
| 2 | index_ai_moreeventtype |  | fid |
