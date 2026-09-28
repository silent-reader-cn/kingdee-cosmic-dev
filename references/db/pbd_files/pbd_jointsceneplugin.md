# 对接场景标准处理配置-pbd_jointsceneplugin

## 对接场景标准处理配置-多语言表 t_pbd_jointsceneplugin_l

- **表名称：** 对接场景标准处理配置-多语言表
- **表名：** t_pbd_jointsceneplugin_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 40 |  | √ | ' ' |  |
| 2 | fname | 配置插件名称 | varchar | 255 |  | √ | ' ' | 配置插件名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_jointsceneplugin_l |  | fid,flocaleid |
| 2 | pk_pbd_jointsceneplugin_l |  | fpkid |

---

## 对接场景标准处理配置-主表 t_pbd_jointsceneplugin

- **表名称：** 对接场景标准处理配置-主表
- **表名：** t_pbd_jointsceneplugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fsceneplugindesc | 对接场景插件功能描述 | varchar | 512 |  | √ | ' ' | 对接场景插件功能描述 |
| 3 | fname | 配置插件名称 | varchar | 512 |  | √ | ' ' | 配置插件名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fchanneltypeid | 对接渠道类型 | varchar | 36 |  | √ | ' ' | [集成渠道类型 pbd_datachanneltype](../pbd_files/pbd_datachanneltype.md) |
| 8 | fpluginsceneid | 插件绑定场景 | varchar | 36 |  | √ | ' ' | [处理场景定义 pbd_scenedefine](../pbd_files/pbd_scenedefine.md) |
| 9 | fnumber | 配置插件编码 | varchar | 80 |  | √ | ' ' | 配置插件编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_jsplugin_fnumber |  | fnumber |
| 2 | pk_pbd_jointsceneplugin |  | fid |
