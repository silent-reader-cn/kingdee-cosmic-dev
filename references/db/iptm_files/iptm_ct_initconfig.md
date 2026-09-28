# 参数设置-iptm_ct_initconfig

## 单据体-子表 t_iptm_ct_initconfiguser

- **表名称：** 单据体-子表
- **表名：** t_iptm_ct_initconfiguser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fexceptionperm | 例外权限 | varchar | 50 |  | √ | ' ' | 例外权限,枚举: 1 :允许新增和修改 2 :允许修改 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_ct_initconfiguser |  | fentryid |
| 2 | idx_iptm_ct_initconfiguser |  | fid |

---

## 配置管控分录-子表 t_iptm_ct_initconfigenv

- **表名称：** 配置管控分录-子表
- **表名：** t_iptm_ct_initconfigenv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangepermtype | 配置修改权限 | varchar | 50 |  | √ | ' ' | 配置修改权限,枚举: 0 :不允许新增和修改 1 :允许新增和修改 2 :允许修改、不允许新增 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcanuploadpacket | 传输包上传/同步 | bpchar | 1 |  | √ | '0' | 传输包上传/同步 |
| 5 | fcanaddpacket | 是否支持添加到传输包 | bpchar | 1 |  | √ | '0' | 是否支持添加到传输包 |
| 6 | fcancreatepacket | 创建传输包 | bpchar | 1 |  | √ | '0' | 创建传输包 |
| 7 | fcandownloadpacket | 传输包下载 | bpchar | 1 |  | √ | '0' | 传输包下载 |
| 8 | fcanmetapack | 元数据打包 | bpchar | 1 |  | √ | '0' | 元数据打包 |
| 9 | fenvtyperemark | 环境说明 | varchar | 200 |  | √ | ' ' | 环境说明 |
| 10 | fcanremotesync | 被远程同步 | bpchar | 1 |  | √ | '0' | 被远程同步 |
| 11 | fenvtypeinfo | 环境类型 | varchar | 50 |  | √ | ' ' | 环境类型,枚举: 0 :配置环境 1 :生产环境 2 :UAT环境 4 :SIT环境 5 :开发环境 6 :非受控环境 |
| 12 | fcanonekeypack | 批量打包 | bpchar | 1 |  | √ | '0' | 批量打包 |
| 13 | fuploadpacketstatus | 传输包状态限制 | varchar | 50 |  | √ | ' ' | 传输包状态限制,枚举: all :无校验 audit :审核状态 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iptm_ct_initconfigenv |  | fid |
| 2 | pk_iptm_ct_initconfigenv |  | fentryid |

---

## 参数设置-主表 t_iptm_ct_initconfig

- **表名称：** 参数设置-主表
- **表名：** t_iptm_ct_initconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillcreatorcover | 制单人信息覆盖策略 | varchar | 50 |  | √ | ' ' | 制单人信息覆盖策略,枚举: no :不处理 all :全部覆盖 |
| 3 | fpacketsecret | 传输包加密密钥 | varchar | 50 |  | √ | ' ' | 传输包加密密钥 |
| 4 | fdefaultkeyfields | 同步默认匹配字段 | varchar | 50 |  | √ | ' ' | 同步默认匹配字段,枚举: id :内码 numberAndOrg :编码+创建组织 |
| 5 | fpacketsecret_enp | fpacketsecret_enp | text | 0 |  |  | null |  |
| 6 | fcomparekey | 动态对象序列化时基础资料如何匹配 | varchar | 50 |  | √ | ' ' | 动态对象序列化时基础资料如何匹配,枚举: 0 :ID相同 1 :编码相同 2 :ID相同或编码相同 3 :ID相同且编码相同 |
| 7 | fpacksizelimit | 传输包大小限制（MB） | int8 | 64 |  | √ | 0 | 传输包大小限制（MB） |
| 8 | fperiodicclean | 定期清理 | bpchar | 1 |  | √ | '0' | 定期清理 |
| 9 | fcleandays | 定期清理间隔(天) | int8 | 64 |  | √ | 0 | 定期清理间隔(天) |
| 10 | fenvrole | 环境类型 | varchar | 50 |  | √ | ' ' | 环境类型,枚举: 5 :开发环境 0 :配置环境 4 :SIT环境 2 :UAT环境 1 :生产环境 6 :非受控环境 |
| 11 | fbasicsetchange | 基础设置新增及修改 | varchar | 50 |  | √ | ' ' | 基础设置新增及修改,枚举: 0 :不允许新增和修改 1 :允许新增和修改 2 :允许修改、不允许新增 |
| 12 | fbatchpackmanualcount | 数据批量处理数量限制 | int8 | 64 |  | √ | 0 | 数据批量处理数量限制 |
| 13 | fstoragepath | 存储路径 | varchar | 50 |  | √ | ' ' | 存储路径 |
| 14 | fconfigtype | 配置管控模式 | varchar | 50 |  | √ | ' ' | 配置管控模式,枚举: 1 :配置弱管控模式 2 :配置强管控模式 |
| 15 | fpackdatalimit | 添加到传输包数量限制 | int8 | 64 |  | √ | 0 | 添加到传输包数量限制 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iptm_ct_initconfig |  | fstoragepath |
| 2 | pk_iptm_ct_initconfig |  | fid |
