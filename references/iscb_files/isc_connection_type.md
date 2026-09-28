# 连接类型-isc_connection_type

## 单据体-子表 t_iscb_cn_type_params

- **表名称：** 单据体-子表
- **表名：** t_iscb_cn_type_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fisrequired | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fparam_length | 最大长度 | int4 | 32 |  | √ | 0 | 最大长度 |
| 6 | fpreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 7 | fenum_values | 枚举值 | varchar | 250 |  | √ | ' ' | 枚举值 |
| 8 | fdefault_value | 默认值 | varchar | 1000 |  | √ | ' ' | 默认值 |
| 9 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 10 | fdesc | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 11 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |
| 12 | fentity_type | 基础资料类型 | varchar | 100 |  | √ | ' ' | 基础资料类型 |
| 13 | fdatatype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: string :字符串 password :密码 long :长整数 checkbox :布尔值 combo :枚举 ref :基础资料 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_cn_type_params |  | fentryid |
| 2 | idx_cntype_param_fid |  | fid |

---

## 连接类型-多语言表 t_iscb_connection_type_l

- **表名称：** 连接类型-多语言表
- **表名：** t_iscb_connection_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | fremark | 描述 | varchar | 1500 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fversiondesc | 版本说明 | varchar | 1500 |  | √ | ' ' | 版本说明 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_connection_type_l_pkey |  | fpkid |
| 2 | idx_iscb_cn_type_l_1 |  | fid |

---

## 连接类型-主表 t_iscb_connection_type

- **表名称：** 连接类型-主表
- **表名：** t_iscb_connection_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fevent_handle_script_tag | 事件处理脚本_详情 | text | 0 |  |  | null | 事件处理脚本_详情 |
| 3 | flogo | logo | varchar | 200 |  | √ | 'default_logo.png' | logo |
| 4 | flogin_script | 会话登录脚本 | varchar | 510 |  | √ | ' ' | 会话登录脚本 |
| 5 | fdomain | 系统所属领域 | varchar | 30 |  | √ | 'L' | 系统所属领域,枚举: A :财务/资源管理（ERP） B :客户关系管理（CRM） C :协同办公管理 D :电商物流 E :社交媒体 F :工具服务软件 G :邮件/信息收发服务 H :人力资源管理 I :金蝶专区 J :开发者系统 K :供应商关系管理（SRM） L :AI人工智能 M :市场营销管理 N :数据库管理 |
| 6 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 7 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 8 | ftest_script | 服务器状态测试脚本 | varchar | 510 |  | √ | ' ' | 服务器状态测试脚本 |
| 9 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 10 | freg_event_script | 订阅脚本 | varchar | 510 |  |  | ' ' | 订阅脚本 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | varchar | 50 |  | √ | ' ' | 主数据内码 |
| 15 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 16 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 17 | ftest_script_tag | 服务器状态测试脚本_详情 | text | 0 |  |  | null | 服务器状态测试脚本_详情 |
| 18 | fscript_extension | 脚本扩展 | varchar | 4000 |  | √ | ' ' | 脚本扩展 |
| 19 | frefresh_script | 会话刷新脚本 | varchar | 510 |  | √ | ' ' | 会话刷新脚本 |
| 20 | fpermit | 连接配置操作权限 | varchar | 255 |  | √ | ',INSERT,UPDATE,DELETE,' | 连接配置操作权限,枚举: INSERT :可新增 UPDATE :可修改 DELETE :可删除 |
| 21 | frefresh_script_tag | 会话刷新脚本_详情 | text | 0 |  |  | null | 会话刷新脚本_详情 |
| 22 | fevent_handle_script | 事件处理脚本 | varchar | 510 |  |  | ' ' | 事件处理脚本 |
| 23 | fremark | 描述 | varchar | 500 |  |  | ' ' | 描述 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fversiondesc | 版本说明 | varchar | 500 |  | √ | ' ' | 版本说明 |
| 26 | fiscustom | 自定义配置 | bpchar | 1 |  | √ | '0' | 自定义配置 |
| 27 | funreg_event_script_tag | 取消订阅脚本_详情 | text | 0 |  |  | null | 取消订阅脚本_详情 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | findex | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 30 | invoke_script | invoke_script | varchar | 510 |  | √ | ' ' |  |
| 31 | fsupport_event_mesh | 支持事件网格 | bpchar | 1 |  | √ | '0' | 支持事件网格 |
| 32 | finvoke_script_tag | API调用脚本_详情 | text | 0 |  |  | null | API调用脚本_详情 |
| 33 | freg_event_script_tag | 订阅脚本_详情 | text | 0 |  |  | null | 订阅脚本_详情 |
| 34 | funreg_event_script | 取消订阅脚本 | varchar | 510 |  |  | ' ' | 取消订阅脚本 |
| 35 | finvoke_script | API调用脚本 | varchar | 510 |  | √ | ' ' | API调用脚本 |
| 36 | fconfig_form | 配置表单 | varchar | 100 |  | √ | ' ' | 配置表单 |
| 37 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 39 | invoke_script_tag | invoke_script_tag | text | 0 |  |  | null |  |
| 40 | ffactory_class | 连接器工厂类 | varchar | 300 |  | √ | ' ' | 连接器工厂类 |
| 41 | flogin_script_tag | 会话登录脚本_详情 | text | 0 |  |  | null | 会话登录脚本_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_cn_type_num |  | fnumber |
| 2 | t_iscb_connection_type_pkey |  | fid |

---

## 单据体-多语言表 t_iscb_cn_type_params_l

- **表名称：** 单据体-多语言表
- **表名：** t_iscb_cn_type_params_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdesc | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | varchar | 36 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_cn_type_params_l |  | fentryid,flocaleid |
| 2 | pk_t_iscb_cn_type_params_l |  | fpkid |
