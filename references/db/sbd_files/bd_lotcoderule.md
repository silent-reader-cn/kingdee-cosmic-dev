# 供应链编码规则-bd_lotcoderule

## 供应链编码规则-主表 t_bd_lotcoderule

- **表名称：** 供应链编码规则-主表
- **表名：** t_bd_lotcoderule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fuseinlot | 适用批号 | bpchar | 1 |  | √ | '1' | 适用批号 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fuseintracknumber | 适用跟踪号 | bpchar | 1 |  | √ | '0' | 适用跟踪号 |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 11 | fuseinserial | 适用序列号 | bpchar | 1 |  | √ | '1' | 适用序列号 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fexample | 编码示例 | varchar | 255 |  | √ | ' ' | 编码示例 |
| 17 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fsplitsign | 段间分隔符 | varchar | 6 |  | √ | ' ' | 段间分隔符 |
| 20 | fmatnumonly | 每个物料单独编码 | bpchar | 1 |  | √ | '1' | 每个物料单独编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_lotcoderule_pkey |  | fid |
| 2 | idx_bd_lotcoderule_num |  | fnumber |

---

## 单据体-子表 t_bd_lotcoderuleentry

- **表名称：** 单据体-子表
- **表名：** t_bd_lotcoderuleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstep | 步长 | int8 | 64 |  | √ | 0 | 步长 |
| 3 | faddstyle | 补位 | varchar | 5 |  | √ | ' ' | 补位,枚举: 1 :右侧 0 :左侧 |
| 4 | flength | 长度 | int8 | 64 |  | √ | 0 | 长度 |
| 5 | fisnumaccord | 流水号依据 | bpchar | 1 |  | √ | '0' | 流水号依据 |
| 6 | fformat | 格式 | varchar | 50 |  | √ | ' ' | 格式 |
| 7 | fformatvalue | 格式值 | varchar | 50 |  | √ | ' ' | 格式值 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fattusingmode | 使用模式 | varchar | 5 |  | √ | ' ' | 使用模式,枚举: A :完全取值 B :属性截断 |
| 10 | flotprop | 编码属性 | int8 | 64 |  | √ | 0 | 供应链编码属性 bd_lotcodeitem |
| 11 | fsettingvalue | 设置值 | varchar | 20 |  | √ | ' ' | 设置值 |
| 12 | faddchar | 补位符号 | varchar | 6 |  | √ | ' ' | 补位符号 |
| 13 | fsplitsign | 段间分隔符 | varchar | 6 |  | √ | ' ' | 段间分隔符 |
| 14 | fcutstyle | 截断 | varchar | 5 |  | √ | ' ' | 截断,枚举: 1 :右侧 0 :左侧 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_lotcoderuleentry_pkey |  | fentryid |
| 2 | idx_bd_lotcoderuleentry_fid |  | fid |

---

## 供应链编码规则-多语言表 t_bd_lotcoderule_l

- **表名称：** 供应链编码规则-多语言表
- **表名：** t_bd_lotcoderule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fexample | 编码示例 | varchar | 255 |  | √ | ' ' | 编码示例 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_lotcoderule_l_fid |  | flocaleid,fid |
| 2 | t_bd_lotcoderule_l_pkey |  | fpkid |
