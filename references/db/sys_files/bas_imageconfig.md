# 影像系统配置-bas_imageconfig

## 影像系统配置-多语言表 t_bas_imageconfig_l

- **表名称：** 影像系统配置-多语言表
- **表名：** t_bas_imageconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 影像前缀 | varchar | 50 |  | √ | ' ' | 影像前缀 |
| 3 | fsimplename | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_bas_imageconfig_l |  | fid,flocaleid |
| 2 | t_bas_imageconfig_l_pkey |  | fpkid |

---

## 影像系统配置-主表 t_bas_imageconfig

- **表名称：** 影像系统配置-主表
- **表名：** t_bas_imageconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fimagesystermip | 影像系统IP | varchar | 50 |  | √ | ' ' | 影像系统IP |
| 4 | fsupportmobile | 支持移动端查看 | bpchar | 1 |  | √ | '0' | 支持移动端查看 |
| 5 | fsupportmult | 支持联查 | bpchar | 1 |  | √ | '0' | 支持联查 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fclientid | client_id | varchar | 50 |  | √ | ' ' | client_id |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fisrandom | 影像编号是否增加随机码 | bpchar | 1 |  | √ | '1' | 影像编号是否增加随机码 |
| 11 | fimageport | 影像端口 | varchar | 50 |  | √ | ' ' | 影像端口 |
| 12 | fispreset | 是否为预置 | bpchar | 1 |  | √ | '0' | 是否为预置 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fclientsecret | client_secret | varchar | 50 |  | √ | ' ' | client_secret |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fimageurl | 影像接口地址 | varchar | 100 |  | √ | ' ' | 影像接口地址 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fimageprotocol | 影像接口协议 | bpchar | 1 |  | √ | ' ' | 影像接口协议,枚举: 1 :http 2 :https |
| 20 | fimageplugin | 影像实现插件 | varchar | 255 |  | √ | ' ' | 影像实现插件 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: B :禁用 A :可用 |
| 22 | fexternalerpid | 所属系统 | int8 | 64 |  | √ | 0 | [业务系统 bas_extenderp](../sys_files/bas_extenderp.md) |
| 23 | fnumber | 编号 | varchar | 50 |  | √ | ' ' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_bas_imageconfig |  | fenable |
| 2 | t_bas_imageconfig_pkey |  | fid |
