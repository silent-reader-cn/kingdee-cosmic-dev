# 配置号编码规则（废弃）-bd_configcoderule

## 单据体-子表 t_bd_configcoderuleentry

- **表名称：** 单据体-子表
- **表名：** t_bd_configcoderuleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsparamode | 截断方式 | bpchar | 1 |  | √ | ' ' | 截断方式,枚举: A :左侧 B :右侧 |
| 3 | ffillsysmbol | 补位符号 | varchar | 10 |  | √ | ' ' | 补位符号 |
| 4 | fsteplength | 步长 | int8 | 64 |  | √ | 0 | 步长 |
| 5 | fformat | 格式 | varchar | 50 |  | √ | ' ' | 格式 |
| 6 | fformatvalue | 格式值 | varchar | 50 |  | √ | ' ' | 格式值 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fcodeattr | 编码属性 | int8 | 64 |  | √ | 0 | [配置号编码属性（废弃） bd_configcodeattr](../sbd_files/bd_configcodeattr.md) |
| 9 | fsetvalue | 设置值 | varchar | 20 |  | √ | ' ' | 设置值 |
| 10 | fentrylength | 长度 | int8 | 64 |  | √ | 0 | 长度 |
| 11 | fusemode | 使用模式 | bpchar | 1 |  | √ | ' ' | 使用模式,枚举: A :完全取值 B :部分截断 |
| 12 | frunnumberjudge | 流水号依据 | bpchar | 1 |  | √ | ' ' | 流水号依据 |
| 13 | fentryseparator | 段间分隔符 | bpchar | 1 |  | √ | ' ' | 段间分隔符 |
| 14 | ffillmode | 补位方式 | bpchar | 1 |  | √ | ' ' | 补位方式,枚举: A :左侧 B :右侧 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_configcoderuleentry |  | fentryid |
| 2 | idx_bd_configcoderuleentry |  | fid |

---

## 配置号编码规则（废弃）-多语言表 t_bd_configcoderule_l

- **表名称：** 配置号编码规则（废弃）-多语言表
- **表名：** t_bd_configcoderule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_configcoderule_l |  | fpkid |
| 2 | idx_bd_configcoderule_l |  | fid,flocaleid |

---

## 配置号编码规则（废弃）-主表 t_bd_configcoderule

- **表名称：** 配置号编码规则（废弃）-主表
- **表名：** t_bd_configcoderule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fenableuser | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fseparator | 段间分隔符 | bpchar | 1 |  | √ | ' ' | 段间分隔符 |
| 15 | fdescription_tag | fdescription_tag | text | 0 |  |  | null |  |
| 16 | fexample | 编码示例 | varchar | 50 |  | √ | ' ' | 编码示例 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_configcoderule_fnumber |  | fnumber |
| 2 | pk_t_bd_configcoderule |  | fid |
