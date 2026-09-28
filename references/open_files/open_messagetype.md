# API消息类型-open_messagetype

## API消息类型-主表 t_open_messagetype

- **表名称：** API消息类型-主表
- **表名：** t_open_messagetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 6 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fappid | 所属应用 | varchar | 50 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fprimitivetype | 原生类型 | varchar | 20 |  | √ | ' ' | 原生类型,枚举: string :字符串 boolean :布尔 date :日期 number :数值 object :对象 array :集合 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fmessagetype | 消息类型 | varchar | 20 |  | √ | ' ' | 消息类型,枚举: primitivetype :原生消息类型 bizobjecttype :业务对象消息类型 customtype :自定义消息类型 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_messagetype |  | fnumber |
| 2 | t_open_messagetype_pkey |  | fid |

---

## API消息类型-多语言表 t_open_messagetype_l

- **表名称：** API消息类型-多语言表
- **表名：** t_open_messagetype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fdiscription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_messagetype_l_fid |  | fid,flocaleid |
| 2 | t_open_messagetype_l_pkey |  | fpkid |

---

## 自定义消息属性分录-多语言表 t_open_custtypeprop_l

- **表名称：** 自定义消息属性分录-多语言表
- **表名：** t_open_custtypeprop_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdiscription | fdiscription | varchar | 500 |  | √ | ' ' |  |
| 2 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_open_custtypeprop_l_pkey |  | fpkid |
| 2 | idx_open_custtypeprop_l_fent |  | fentryid,flocaleid |

---

## 自定义消息属性分录-子表 t_open_custtypeprop

- **表名称：** 自定义消息属性分录-子表
- **表名：** t_open_custtypeprop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequired | 是否必录 | bpchar | 1 |  |  | '0' | 是否必录 |
| 3 | fexclusivemaximum | 包括最大值 | bpchar | 1 |  |  | '0' | 包括最大值 |
| 4 | fpropname | 属性名称 | varchar | 100 |  |  | null | 属性名称 |
| 5 | fexclusiveminimum | 包括最小值 | bpchar | 1 |  |  | '0' | 包括最小值 |
| 6 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 7 | maximum | maximum | varchar | 50 |  |  | null |  |
| 8 | fpattern | 正则表达式 | varchar | 200 |  | √ | ' ' | 正则表达式 |
| 9 | fproptype | 属性类型 | int8 | 64 |  |  | null | API消息类型 open_messagetype |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | minimum | minimum | varchar | 50 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_open_custtypeprop_pkey |  | fentryid |
| 2 | idx_open_custtypeprop_fid |  | fid |
