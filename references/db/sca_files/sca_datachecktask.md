# 数据检查任务-sca_datachecktask

## 数据检查任务-主表 t_sca_datachecktask

- **表名称：** 数据检查任务-主表
- **表名：** t_sca_datachecktask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 1 :启用 0 :禁用 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | foperatorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | freceiverid | 消息接收人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 8 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 9 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_datachecktask |  | fnumber,fappnum |
| 2 | t_sca_datachecktask_pkey |  | fid |

---

## 单据体-子表 t_sca_datachecktaskentry

- **表名称：** 单据体-子表
- **表名：** t_sca_datachecktaskentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 操作级别 | varchar | 30 |  | √ | ' ' | 操作级别,枚举: A :提醒 B :自动生成 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fopcycle | 操作周期 | varchar | 30 |  | √ | ' ' | 操作周期,枚举: A :每半天 B :每日 C :每周 D :每月 E :不重复 |
| 5 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | 数据检查项 sca_datacheckitem |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_datachecktaskentry_pkey |  | fentryid |
| 2 | idx_sca_datachecktaskentry |  | fid,fcheckitemid |

---

## 数据检查任务-多语言表 t_sca_datachecktask_l

- **表名称：** 数据检查任务-多语言表
- **表名：** t_sca_datachecktask_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_datachecktask_l |  | fname |
| 2 | t_sca_datachecktask_l_pkey |  | fpkid |
