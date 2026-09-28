# 发票类电子凭证池数据查询接口-evp_queryinterface

## 发票类电子凭证池数据查询接口-主表 t_evp_queryinterface

- **表名称：** 发票类电子凭证池数据查询接口-主表
- **表名：** t_evp_queryinterface

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 5 | fdatasize | 拉取数据大小 | int4 | 32 |  | √ | 0 | 拉取数据大小 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | felevouchertypeid | 单据类型 | varchar | 50 |  |  | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 9 | fdescription | 描述说明 | varchar | 255 |  | √ | ' ' | 描述说明 |
| 10 | fpluginname | 插件名 | varchar | 255 |  | √ | ' ' | 插件名 |
| 11 | fversion | 适用版本 | varchar | 50 |  | √ | ' ' | 适用版本 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evp_queryinterface |  | felevouchertypeid |
| 2 | pk_t_evp_queryinterface |  | fid |
