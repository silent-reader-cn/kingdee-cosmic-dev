# 用户身份配置-cbi_agent_role_config

## 用户身份配置-子表 t_cbi_role_config

- **表名称：** 用户身份配置-子表
- **表名：** t_cbi_role_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuperior | 身份信息上级 | varchar | 1000 |  | √ | ' ' | 身份信息上级 |
| 3 | fdimensionvalue | 选择用户身份信息 | varchar | 255 |  | √ | ' ' | 选择用户身份信息,枚举: |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fuserid | 姓名 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fdimension | 选择身份所属维度 | varchar | 255 |  | √ | ' ' | 选择身份所属维度,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_role_config_fk |  | fid |
| 2 | pk_cbi_role_config |  | fentryid |

---

## 用户身份配置-主表 t_cbi_agent_role_config

- **表名称：** 用户身份配置-主表
- **表名：** t_cbi_agent_role_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 5 | fagentbaseid | 智能体 | int8 | 64 |  | √ | 0 | [智能体 cbi_agent_base](../chatbi_files/cbi_agent_base.md) |
| 6 | fmodifytime | 修改日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_agent_role_config_fk |  | fagentbaseid |
| 2 | pk_cbi_agent_role_config |  | fid |
