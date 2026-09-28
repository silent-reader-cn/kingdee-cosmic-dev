# 外部系统类型-isc_connection_type_x

## 外部系统类型-多语言表 t_isc_connection_type_x_l

- **表名称：** 外部系统类型-多语言表
- **表名：** t_isc_connection_type_x_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cn_type_l_1 |  | fid |
| 2 | pk_t_isc_connection_type_x_l |  | fpkid |

---

## 外部系统类型-主表 t_isc_connection_type_x

- **表名称：** 外部系统类型-主表
- **表名：** t_isc_connection_type_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fremark | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | flogin_script | 会话登录脚本 | varchar | 510 |  | √ | ' ' | 会话登录脚本 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | findex | 顺序号 | int4 | 32 |  | √ | 0 | 顺序号 |
| 7 | ftest_script | 服务器状态测试脚本 | varchar | 510 |  | √ | ' ' | 服务器状态测试脚本 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | finvoke_script_tag | API调用脚本_详情 | text | 0 |  |  | null | API调用脚本_详情 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | varchar | 50 |  | √ | ' ' | 主数据内码 |
| 13 | fpreset | 是否预置 | bpchar | 1 |  | √ | '1' | 是否预置 |
| 14 | finvoke_script | API调用脚本 | varchar | 510 |  | √ | ' ' | API调用脚本 |
| 15 | ftest_script_tag | 服务器状态测试脚本_详情 | text | 0 |  |  | null | 服务器状态测试脚本_详情 |
| 16 | fconfig_form | 配置表单 | varchar | 100 |  | √ | ' ' | 配置表单 |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fscript_extension | 脚本扩展 | varchar | 4000 |  | √ | ' ' | 脚本扩展 |
| 19 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 20 | ffactory_class | 连接器工厂 | varchar | 300 |  | √ | ' ' | 连接器工厂 |
| 21 | flogin_script_tag | 会话登录脚本_详情 | text | 0 |  |  | null | 会话登录脚本_详情 |
| 22 | frefresh_script | 会话刷新脚本 | varchar | 510 |  | √ | ' ' | 会话刷新脚本 |
| 23 | fpermit | 连接配置操作权限 | varchar | 255 |  | √ | ' ' | 连接配置操作权限,枚举: INSERT :可新增 UPDATE :可修改 DELETE :可删除 |
| 24 | frefresh_script_tag | 会话刷新脚本_详情 | text | 0 |  |  | null | 会话刷新脚本_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_connection_type_x |  | fid |
| 2 | idx_cn_type_x_1 |  | fnumber |
