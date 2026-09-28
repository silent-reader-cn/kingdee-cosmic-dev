# 供应商画像配置-srm_portrait_config

## 供应商画像配置-多语言表 t_srm_portrait_config_l

- **表名称：** 供应商画像配置-多语言表
- **表名：** t_srm_portrait_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_portrait_config_l |  | fpkid |
| 2 | idx_t_portrait_con_l_fid |  | fid,flocaleid |

---

## 供应商画像配置-主表 t_srm_portrait_config

- **表名称：** 供应商画像配置-主表
- **表名：** t_srm_portrait_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsubpage | 子页面标识 | varchar | 50 |  | √ | ' ' | 子页面标识,枚举: srm_portrait_access :准入认证 srm_portrait_source :寻源管理 srm_portrait_contract :合同管理 srm_portrait_purchases :采购执行 srm_portrait_kpi :绩效评估 srm_portrait_compare :询比价 :无 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | findicatorplugin | 指标插件 | varchar | 100 |  | √ | ' ' | 指标插件 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 13 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_portrait_config_fnum |  | fnumber |
| 2 | pk_t_srm_portrait_config |  | fid |
