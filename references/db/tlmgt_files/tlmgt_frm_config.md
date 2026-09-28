# 处理器配置-tlmgt_frm_config

## 处理器配置-主表 t_tlmgt_frm_config

- **表名称：** 处理器配置-主表
- **表名：** t_tlmgt_frm_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresourcefiletype | 资源文件类型 | varchar | 64 |  | √ | ' ' | 资源文件类型,枚举: multilang_table :多语言库表类型 back_end :后端资源类型 web_app :前端资源类型 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fdomain | 领域标识 | varchar | 64 |  | √ | ' ' | 领域标识 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fprocessparam | 处理器执行参数 | varchar | 1024 |  | √ | ' ' | 处理器执行参数 |
| 7 | fwordtype | 词条类型 | int8 | 64 |  | √ | 0 | [词条类型 tlmgt_wordtype](../tlmgt_files/tlmgt_wordtype.md) |
| 8 | fprocessor | 处理器 | int8 | 64 |  | √ | 0 | [处理器基础资料 tlmgt_frm_processor](../tlmgt_files/tlmgt_frm_processor.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 32 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmodule | 模块标识 | varchar | 64 |  | √ | ' ' | 模块标识 |
| 14 | fenable | 使用状态 | varchar | 32 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fresource | 资源标识 | varchar | 64 |  | √ | ' ' | 资源标识 |
| 16 | fnumber | 编码 | varchar | 32 |  | √ | ' ' | 编码 |
| 17 | fdatatype | 词条数据类型 | varchar | 64 |  | √ | ' ' | 词条数据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tlmgt_frm_config |  | fid |
| 2 | idx_t_tlmgt_frm_conf |  | fnumber |

---

## 处理器配置-多语言表 t_tlmgt_frm_config_l

- **表名称：** 处理器配置-多语言表
- **表名：** t_tlmgt_frm_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tlmgt_frm_conf_l |  | fid |
| 2 | pk_t_tlmgt_frm_config_l |  | fpkid |
