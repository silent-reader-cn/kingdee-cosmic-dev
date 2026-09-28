# 对接场景标准处理配置-pbd_jointsceneplugin

## 对接场景标准处理配置-主表 t_pbd_jointsceneplugin

- **表名称：** 对接场景标准处理配置-主表
- **表名：** t_pbd_jointsceneplugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fsceneplugindesc | 对接场景插件功能描述 | varchar | 512 |  | √ | ' ' | 对接场景插件功能描述 |
| 3 | fname | 配置插件名称 | varchar | 512 |  | √ | ' ' | 配置插件名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fchanneltypeid | 对接渠道类型 | varchar | 36 |  | √ | ' ' | 集成渠道类型 pbd_datachanneltype |
| 8 | fpluginsceneid | 插件绑定场景 | varchar | 36 |  | √ | ' ' | 处理场景定义 pbd_scenedefine |
| 9 | fnumber | 配置插件编码 | varchar | 80 |  | √ | ' ' | 配置插件编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_jointsceneplugin |  | fid |
| 2 | idx_pbd_jsplugin_fnumber |  | fnumber |
