# 处理器配置-inte_processorconfig_frm

## 处理器配置-多语言表 t_int_processconf_frm_l

- **表名称：** 处理器配置-多语言表
- **表名：** t_int_processconf_frm_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 64 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_int_proconf_l |  | fid |
| 2 | pk_t_int_processconf_frm_l |  | fpkid |

---

## 处理器配置-主表 t_int_processconf_frm

- **表名称：** 处理器配置-主表
- **表名：** t_int_processconf_frm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 64 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdomain | 领域标识 | varchar | 255 |  | √ | ' ' | 领域标识 |
| 6 | fmatchtime | 匹配时机 | varchar | 50 |  | √ | ' ' | 匹配时机,枚举: EXTRACT :抽取 APPLY :应用 BUILD :构建 |
| 7 | fwordtype | 词条类型 | int8 | 64 |  | √ | 0 | 词条类型 inte_wordtype_frm |
| 8 | fprocessor | 处理器 | int8 | 64 |  | √ | 0 | 处理器基础资料 inte_processor_frm |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 32 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fresourcetype | 资源服务类型 | varchar | 50 |  | √ | ' ' | 资源服务类型,枚举: BACK_END :后端资源类型 WEB_APP :前端资源类型 MULTILANG_TABLE :多语言库表类型 CONFIG_FILE :配置文件类型 |
| 14 | fmodule | 模块标识 | varchar | 255 |  | √ | ' ' | 模块标识 |
| 15 | fenable | 使用状态 | varchar | 32 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 64 |  | √ | ' ' | 编码 |
| 17 | fresource | 资源标识 | varchar | 255 |  | √ | ' ' | 资源标识 |
| 18 | fdatatype | 词条数据类型 | int8 | 64 |  | √ | 0 | 词条数据类型 inte_datatype_frm |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_int_prcconfig |  | fnumber |
| 2 | pk_t_int_processconf_frm |  | fid |
