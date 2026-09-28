# 归档反写配置-aef_archivewriteconfig

## 归档反写配置-主表 t_aef_archivewriteconfig

- **表名称：** 归档反写配置-主表
- **表名：** t_aef_archivewriteconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcouldid | 云id | varchar | 50 |  | √ | ' ' | 云id |
| 3 | fwritebackplugin | 反写插件 | varchar | 255 |  | √ | ' ' | 反写插件 |
| 4 | fbilltype | 单据 | varchar | 40 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fappid | appid | varchar | 50 |  | √ | ' ' | appid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aef_archivewriteconfig |  | fbilltype |
| 2 | pk_t_aef_archivewriteconfig |  | fid |
