# 连接配置-chatbi_assistant

## 适用主题-多选基础资料表 t_gai_cbi_assistant_theme

- **表名称：** 适用主题-多选基础资料表
- **表名：** t_gai_cbi_assistant_theme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [主题基础资料 gai_cbi_theme_basedata](../chatbi_files/gai_cbi_theme_basedata.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_cbi_assistant_theme_fk |  | fentryid |
| 2 | pk_gai_cbi_assistant_theme |  | fpkid |

---

## 连接配置-分表 t_cbi_assistant_a

- **表名称：** 连接配置-分表
- **表名：** t_cbi_assistant_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fphone | phone | varchar | 50 |  |  | ' ' | phone |
| 3 | fappsecret | AppSecret | varchar | 200 |  |  | ' ' | AppSecret |
| 4 | fdomain | 域名 | varchar | 200 |  |  | ' ' | 域名 |
| 5 | faccountname | 数据中心名称 | varchar | 200 |  |  | ' ' | 数据中心名称 |
| 6 | fgatewayparam | 网关参数 | varchar | 150 |  |  | ' ' | 网关参数 |
| 7 | fappsecret_enp | fappsecret_enp | varchar | 500 |  |  | null |  |
| 8 | fassistantnumber | 助手 | varchar | 100 |  |  | ' ' | 助手 |
| 9 | frealnumcheck | App端使用真实手机号码作为验权账号 | bpchar | 1 |  |  | '0' | App端使用真实手机号码作为验权账号 |
| 10 | faccountid | 数据中心ID | varchar | 50 |  |  | ' ' | 数据中心ID |
| 11 | fappid | AppId | varchar | 50 |  |  | ' ' | AppId |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cbi_assistant_a_id |  | fid |

---

## 连接配置-分表 t_cbi_assistant_d

- **表名称：** 连接配置-分表
- **表名：** t_cbi_assistant_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdomian | 域名 | varchar | 100 |  |  | ' ' | 域名 |
| 3 | fapikey | API密钥 | varchar | 200 |  |  | ' ' | API密钥 |
| 4 | fgatewayauthconfig | 网关认证配置 | varchar | 100 |  |  | ' ' | 网关认证配置 |
| 5 | fgatewayauthtype | 网关认证类型 | varchar | 10 |  | √ | '0' | 网关认证类型,枚举: 1 :URL参数 2 :Header 0 :无 |
| 6 | fmultipleapikey | 多数据集API密钥 | varchar | 50 |  | √ | ' ' | 多数据集API密钥 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cbi_assistant_d_id |  | fid |

---

## 连接配置-主表 t_cbi_assistant

- **表名称：** 连接配置-主表
- **表名：** t_cbi_assistant

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpicture | 图片字段 | varchar | 255 |  |  | ' ' | 图片字段 |
| 3 | fname | 名称 | varchar | 200 |  |  | ' ' | 名称 |
| 4 | finputtips | 输入提示 | varchar | 2000 |  |  | ' ' | 输入提示 |
| 5 | ftype | 类型 | varchar | 50 |  |  | ' ' | 类型,枚举: agent :苍穹Agent dify :Dify |
| 6 | fintroduce | 引导语 | varchar | 2000 |  |  | ' ' | 引导语 |
| 7 | fenable | 状态 | bpchar | 1 |  |  | '1' | 状态,枚举: 0 :禁用 1 :启用 |
| 8 | fnumber | 编码 | varchar | 50 |  |  | ' ' | 编码 |
| 9 | fdesc | 描述 | varchar | 500 |  |  | ' ' | 描述 |
| 10 | fvoice | 是否开启语音功能 | bpchar | 1 |  | √ | '0' | 是否开启语音功能 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cbi_assistant_id |  | fid |

---

## 单据体-子表 t_gai_cbi_assistant_conn

- **表名称：** 单据体-子表
- **表名：** t_gai_cbi_assistant_conn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fappsecret | AppSecret | varchar | 255 |  | √ | ' ' | AppSecret |
| 3 | fdomain | 域名 | varchar | 255 |  | √ | ' ' | 域名 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fgatewayauthtype | 网关认证类型 | varchar | 50 |  | √ | ' ' | 网关认证类型,枚举: 1 :URL参数 2 :Header 0 :无 |
| 6 | fappid | Appid | varchar | 50 |  | √ | ' ' | Appid |
| 7 | fappsecret_enp | fappsecret_enp | varchar | 2000 |  | √ | ' ' |  |
| 8 | frealnumcheck | App端使用真实手机号码作为验权账号 | varchar | 50 |  | √ | ' ' | App端使用真实手机号码作为验权账号 |
| 9 | fname | 连接名称 | varchar | 255 |  | √ | ' ' | 连接名称 |
| 10 | fphone | phone | varchar | 50 |  | √ | ' ' | phone |
| 11 | fworkflowid | 工作流 | int8 | 64 |  | √ | 0 | [工作流基础资料 chatbi_workflow_base](../chatbi_files/chatbi_workflow_base.md) |
| 12 | faccountname | 数据中心名称 | varchar | 255 |  | √ | ' ' | 数据中心名称 |
| 13 | fadapt | 适用范围 | varchar | 50 |  | √ | ' ' | 适用范围,枚举: basic :所有主题 agents :所有智能体 specified :指定主题 agent :指定智能体 |
| 14 | fgatewayauthconfig | 网关认证配置 | varchar | 255 |  | √ | ' ' | 网关认证配置 |
| 15 | fmultipleapikey | 多数据集API秘钥 | varchar | 255 |  | √ | ' ' | 多数据集API秘钥 |
| 16 | fgatewayauthconfig_enp | fgatewayauthconfig_enp | varchar | 2000 |  | √ | ' ' |  |
| 17 | ftype | 连接类型 | varchar | 50 |  | √ | ' ' | 连接类型,枚举: agent :苍穹Agent dify :Dify workflowengine :工作流 |
| 18 | fapikey | API秘钥 | varchar | 255 |  | √ | ' ' | API秘钥 |
| 19 | fgatewayparam | 网关参数 | varchar | 500 |  | √ | ' ' | 网关参数 |
| 20 | fenable | 启用 | varchar | 50 |  | √ | '0' | 启用 |
| 21 | fapikey_enp | fapikey_enp | varchar | 2000 |  | √ | ' ' |  |
| 22 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 23 | fassistantnumber | 助手 | varchar | 50 |  | √ | ' ' | 助手 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | faccountid | 数据中心ID | varchar | 255 |  | √ | ' ' | 数据中心ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_cbi_assistant_conn_fentryid |  | fentryid |

---

## 适用智能体-多选基础资料表 t_gai_cbi_assistant_agent

- **表名称：** 适用智能体-多选基础资料表
- **表名：** t_gai_cbi_assistant_agent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [智能体 cbi_agent_base](../chatbi_files/cbi_agent_base.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_cbi_assistant_agent |  | fentryid |
| 2 | pk_gai_cbi_assistant_agent |  | fpkid |
