# 全文检索输出-pbd_esoutput

## 字段单据体-子表 t_pbd_esoutputentry

- **表名称：** 字段单据体-子表
- **表名：** t_pbd_esoutputentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fevalpath | 取值表达式 | varchar | 255 |  | √ | ' ' | 取值表达式 |
| 3 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :是/否 ENUM :枚举 STRUCT :结构 |
| 4 | fisarray | 是否多值 | bpchar | 1 |  | √ | '0' | 是否多值 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 7 | fesmappingid | 取自es属性 | int8 | 64 |  | √ | 0 | 全文检索映射属性 pbd_esmapping_property |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fcandidatekey | 是否候选键 | bpchar | 1 |  | √ | '0' | 是否候选键 |
| 10 | ffieldkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 11 | ffixevalue | 直接赋值 | varchar | 255 |  | √ | ' ' | 直接赋值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_esoutputentry |  | fentryid |
| 2 | idx_pbd_esoutputentry_id |  | fid |

---

## 全文检索输出-主表 t_pbd_esoutput

- **表名称：** 全文检索输出-主表
- **表名：** t_pbd_esoutput

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | findexentityid | 索引实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 13 | ftargetid | 目标实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_esoutput |  | fid |
| 2 | idx_pbd_esoutput_fnumber |  | fnumber |

---

## 全文检索输出-多语言表 t_pbd_esoutput_l

- **表名称：** 全文检索输出-多语言表
- **表名：** t_pbd_esoutput_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_esoutput_l |  | fpkid |
| 2 | idx_pbd_esoutput_l_fid |  | fid |
