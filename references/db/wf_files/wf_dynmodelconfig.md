# 动态模型配置-wf_dynmodelconfig

## 动态模型配置-主表 t_wf_dynmodelconfig

- **表名称：** 动态模型配置-主表
- **表名：** t_wf_dynmodelconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuiltin | 内置配置 | bpchar | 1 |  | √ | '0' | 内置配置 |
| 3 | flifecycleconfig | 生命周期配置 | varchar | 3000 |  | √ | ' ' | 生命周期配置 |
| 4 | fcustomruntimeconfig | 自定义运行时配置 | text | 0 |  |  | null | 自定义运行时配置 |
| 5 | fmandatory | 是否必选 | bpchar | 1 |  | √ | '0' | 是否必选 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fisv | 开发商标识 | varchar | 30 |  | √ | 'kingdee' | 开发商标识 |
| 8 | fappid | 应用ID | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcloudid | 云ID | varchar | 500 |  | √ | ' ' | 云ID |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcustomuiconfig | 自定义界面配置 | text | 0 |  |  | null | 自定义界面配置 |
| 14 | fstenciltype | 节点类型 | varchar | 100 |  | √ | ' ' | 节点类型 |
| 15 | fstenciltypename | 节点类型名称 | varchar | 100 |  | √ | ' ' | 节点类型名称 |
| 16 | fcustomdefconfig | 自定义节点默认配置 | text | 0 |  |  | null | 自定义节点默认配置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_dynmodelconfig_pkey |  | fid |
| 2 | idx_wf_dynmodelconfig_appid |  | fappid |
