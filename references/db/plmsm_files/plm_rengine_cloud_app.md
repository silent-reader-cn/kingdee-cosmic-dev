# 规则引擎云与应用（规则引擎）-plm_rengine_cloud_app

## 规则引擎云与应用（规则引擎）-主表 t_plm_egn_cloudapp

- **表名称：** 规则引擎云与应用（规则引擎）-主表
- **表名：** t_plm_egn_cloudapp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | findex | 排序号 | int8 | 64 |  | √ | 0 | 排序号 |
| 6 | fappname | 应用名称 | varchar | 255 |  | √ | ' ' | 应用名称 |
| 7 | finitdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :手工录入 1 :初始化 |
| 8 | finitstatus | 初始化状态 | varchar | 50 |  | √ | ' ' | 初始化状态,枚举: 0 :进行中 1 :已验证 2 :已完成 |
| 9 | fissyspreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 10 | finitbatch | 初始化批次 | int8 | 64 |  | √ | 0 | 初始化批次 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体（规则引擎） plm_rengine_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_egn_cloudapp |  | fappid |
| 2 | pk_t_plm_egn_cloudapp |  | fid |

---

## 规则引擎云与应用（规则引擎）-多语言表 t_plm_egn_cloudapp_l

- **表名称：** 规则引擎云与应用（规则引擎）-多语言表
- **表名：** t_plm_egn_cloudapp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
