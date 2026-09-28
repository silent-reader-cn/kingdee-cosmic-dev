# 提示语工程配置-tlmgt_basedata_config

## 提示语工程配置-多语言表 t_tlmgt_basedata_config_l

- **表名称：** 提示语工程配置-多语言表
- **表名：** t_tlmgt_basedata_config_l

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
| 1 | idx_t_tlmgt_basedata_l |  | fid |
| 2 | pk_t_tlmgt_basedata_config_l |  | fpkid |

---

## 提示语工程配置-主表 t_tlmgt_basedata_config

- **表名称：** 提示语工程配置-主表
- **表名：** t_tlmgt_basedata_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 32 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fresourcetype | 资源类型 | int8 | 64 |  | √ | 0 | [资源类型 tlmgt_resource_type](../tlmgt_files/tlmgt_resource_type.md) |
| 7 | fapp | 所属应用 | varchar | 32 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | ' ' | 是否系统预置 |
| 10 | fenable | 使用状态 | varchar | 32 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 工程编码 | varchar | 32 |  | √ | ' ' | 工程编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tlmgt_bs_conf |  | fnumber |
| 2 | pk_t_tlmgt_basedata_config |  | fid |
