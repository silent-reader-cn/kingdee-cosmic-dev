# 服务商扩展插件设置-er_biz_info_plugin

## 扩展插件信息-子表 t_er_bizinfo_plugindetail

- **表名称：** 扩展插件信息-子表
- **表名：** t_er_bizinfo_plugindetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fclasspath | 插件类路径 | varchar | 200 |  | √ | ' ' | 插件类路径 |
| 6 | ffunction | 功能 | varchar | 50 |  | √ | ' ' | 功能,枚举: orgInvoke :组织 userInvoke :人员 tripReqBillInvoke :出差申请单 loginInvoke :登录 orderInvoke :订单 checkingInvoke :结算单 invoiceSendInvoke :发票开具 invoiceReceiveInvoke :发票接收 orderUpdateInvoke :订单t+2 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_plugin_ffunction |  | fid,ffunction |
| 2 | t_er_bizinfo_plugindetail_pkey |  | fdetailid |

---

## 服务商扩展插件设置-主表 t_er_bizinfo_plugin

- **表名称：** 服务商扩展插件设置-主表
- **表名：** t_er_bizinfo_plugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnumber | 服务商 | varchar | 80 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 MEITUAN :美团 GAODE :高德 TONGCHENG :同程 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_bizinfo_plugin_fnumber |  | fnumber |
| 2 | t_er_bizinfo_plugin_pkey |  | fid |
