# 渠道云数据升级-ocdbd_dataupdate

## 渠道云数据升级-主表 t_ocdbd_dataupdate

- **表名称：** 渠道云数据升级-主表
- **表名：** t_ocdbd_dataupdate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrinfo | 异常信息 | varchar | 2000 |  | √ | ' ' | 异常信息 |
| 3 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fexecount | 执行次数 | int4 | 32 |  | √ | 0 | 执行次数 |
| 6 | flastexecutime | 最后执行时间 | timestamp | 0 |  |  | null | 最后执行时间 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fupdateplugin | 升级插件 | varchar | 200 |  | √ | ' ' | 升级插件 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fexecustatus | 执行状态 | bpchar | 1 |  | √ | 'A' | 执行状态,枚举: A :未执行 B :执行成功 C :执行失败 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_dataupdate |  | fid |
| 2 | idx_ocdbd_plugin |  | fupdateplugin |

---

## 渠道云数据升级-多语言表 t_ocdbd_dataupdate_l

- **表名称：** 渠道云数据升级-多语言表
- **表名：** t_ocdbd_dataupdate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_dataupdate_l |  | fpkid |
| 2 | idx_ocdbd_dataupfid |  | fid |
