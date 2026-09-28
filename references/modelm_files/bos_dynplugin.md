# 动态插件定义-bos_dynplugin

## 动态插件定义-主表 t_meta_dynplugin

- **表名称：** 动态插件定义-主表
- **表名：** t_meta_dynplugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 事件 | varchar | 255 |  | √ | ' ' | 事件 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | finterfacetype | 接口类型 | bpchar | 1 |  | √ | '1' | 接口类型,枚举: 1 :表单插件 2 :单据插件 3 :列表插件 4 :操作插件 |
| 5 | feventmethod | 事件 | varchar | 255 |  | √ | ' ' | 事件,枚举: |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 7 | fclassname | 插件路径 | varchar | 255 |  | √ | ' ' | 插件路径 |
| 8 | fisv | 开发商标识 | varchar | 200 |  | √ | ' ' | 开发商标识 |
| 9 | frole | 作用范围 | bpchar | 1 |  | √ | '1' | 作用范围,枚举: 1 :布局 2 :实体 |
| 10 | fbizappid | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fplugincode | 代码 | varchar | 255 |  |  | ' ' | 代码 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fplugindesc_tag | 插件说明_详情 | text | 0 |  |  | null | 插件说明_详情 |
| 17 | fcodetype | 代码类型 | bpchar | 1 |  | √ | '0' | 代码类型,枚举: 0 :Java 4 :KingScript |
| 18 | fnumber | 唯一名称标识 | varchar | 200 |  | √ | ' ' | 唯一名称标识 |
| 19 | fplugindesc | 插件说明 | varchar | 255 |  |  | ' ' | 插件说明 |
| 20 | fplugincode_tag | 代码_详情 | text | 0 |  |  | null | 代码_详情 |
| 21 | fclient | 客户端 | bpchar | 1 |  | √ | '1' | 客户端,枚举: 1 :PC端 2 :移动端 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_dynplugin_method |  | feventmethod |
| 2 | pk_meta_dynplugin |  | fid |

---

## 动态插件定义-多语言表 t_meta_dynplugin_l

- **表名称：** 动态插件定义-多语言表
- **表名：** t_meta_dynplugin_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 事件 | varchar | 255 |  | √ | ' ' | 事件 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_dynplugin_l_id |  | fid,flocaleid |
| 2 | pk_meta_dynplugin_l |  | fpkid |
