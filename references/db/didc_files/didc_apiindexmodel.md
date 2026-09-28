# API指标模型-didc_apiindexmodel

## 字段元数据-子表 t_didc_apiindex_metas

- **表名称：** 字段元数据-子表
- **表名：** t_didc_apiindex_metas

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldnumber | 字段编码 | varchar | 255 |  | √ | ' ' | 字段编码 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: DIMENSION :维度 INDEX :指标 |
| 4 | fdisplayname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 5 | fformula | 计算公式 | varchar | 255 |  | √ | ' ' | 计算公式 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: TEXT :文本 NUM :数值 DATE :日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_apiindex_metas_fk |  | fid |
| 2 | pk_didc_apiindex_metas |  | fentryid |

---

## API指标模型-多语言表 t_didc_apiindexmodel_l

- **表名称：** API指标模型-多语言表
- **表名：** t_didc_apiindexmodel_l

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
| 1 | idx_didc_apiindexmodel_l_0 |  | fid,flocaleid |
| 2 | pk_didc_apiindexmodel_l |  | fpkid |

---

## API指标模型-主表 t_didc_apiindexmodel

- **表名称：** API指标模型-主表
- **表名：** t_didc_apiindexmodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodel | 模型标识 | varchar | 255 |  | √ | ' ' | 模型标识 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fdataurl | 数据服务 | varchar | 255 |  | √ | ' ' | 数据服务 |
| 6 | fapienv | 连接环境 | int8 | 64 |  | √ | 0 | [API环境配置 didc_api_env](../didc_files/didc_api_env.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmetaurl | 元数据服务 | varchar | 255 |  | √ | ' ' | 元数据服务 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fappid | 应用标识 | varchar | 50 |  | √ | ' ' | 应用标识 |
| 11 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcloudid | 云标识 | varchar | 50 |  | √ | ' ' | 云标识 |
| 15 | fservicename | 服务名称 | varchar | 50 |  | √ | ' ' | 服务名称 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_apiindexmodel_m0 |  | fmasterid |
| 2 | pk_didc_apiindexmodel |  | fid |
