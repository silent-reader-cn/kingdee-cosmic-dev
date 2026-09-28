# 第三方应用插件配置-bos_thirdapp_plugin

## 第三方应用插件配置-主表 t_bas_thirdapps_plugin

- **表名称：** 第三方应用插件配置-主表
- **表名：** t_bas_thirdapps_plugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpluginconfig | 插件配置按钮组 | bpchar | 1 |  | √ | '0' | 插件配置按钮组,枚举: 1 :标准插件 2 :自定义插件 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fimtypeid | 第三方映射 | int8 | 64 |  | √ | 0 | [移动平台类型 bas_instantmsgtype](../base_files/bas_instantmsgtype.md) |
| 7 | fpluginname | 插件名 | varchar | 50 |  | √ | ' ' | 插件名 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_thirdapps_plugin |  | fid |
| 2 | idx_thirdapps_plugin_imtypeid |  | fimtypeid |
